import json
def mostrar_productos_servicios():
    with open('Productos_y_Servicios/PyS.json', 'r') as file:
        datos = json.load(file)
        print(datos)
        print("Productos Disponibles:")
        for producto, detalles in datos["Productos"].items():
            print(f"{producto}: {detalles['Precio']}")
        print("\nServicios Disponibles:")
        for servicio, precio in datos["Servicios"].items():
            print(f"{servicio}: {precio}")

def comprar_producto_servicio(usuario, eleccion, cantidad=1):
    # Cargar los datos de usuarios
    with open('Usuarios/Datos_Usuarios.json', 'r') as file:
        usuarios = json.load(file)

    # Actualizar datos del usuario
    for user in usuarios:
        if user["Nombre"] == usuario:
            # Actualizar datos de compra
            if eleccion in user:
                user[eleccion] += cantidad
            else:
                user[eleccion] = cantidad

    # Guardar los datos actualizados
    with open('Usuarios/Datos_Usuarios.json', 'w') as file:
        json.dump(usuarios, file)

    # Registrar la compra en el contador
    with open('Productos_y_Servicios/PyS.json', 'r+') as file:
        data = json.load(file)
        if eleccion in data["Productos"]:
            if "Productos Populares" in data:
                if eleccion in data["Productos Populares"]:
                    data["Productos Populares"][eleccion] += cantidad
                else:
                    data["Productos Populares"][eleccion] = cantidad
            else:
                data["Productos Populares"] = {eleccion: cantidad}
        elif eleccion in data["Servicios"]:
            if "Servicios Populares" in data:
                if eleccion in data["Servicios Populares"]:
                    data["Servicios Populares"][eleccion] += cantidad
                else:
                    data["Servicios Populares"][eleccion] = cantidad
            else:
                data["Servicios Populares"] = {eleccion: cantidad}
        
        # Escribir los datos actualizados
        json.dump(data, file)