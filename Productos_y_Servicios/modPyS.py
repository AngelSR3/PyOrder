import json

def cargar_datos(archivo):
    with open(archivo, "r") as file:
        datos = json.load(file)
    return datos
        
def guardar_datos(datos, archivo):
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)

def mostrar_productos_servicios():
    datos = cargar_datos('Productos_y_Servicios/PyS.json')
    print("Productos Disponibles:")
    for producto, detalles in datos["Productos"].items():
        print(f"{producto}: {detalles['Precio']}")
    print("\nServicios Disponibles:")
    for servicio, precio in datos["Servicios"].items():
        print(f"{servicio}: {precio}")

def comprar_producto_servicio(usuario, eleccion, cantidad=1):
    # Cargar los datos de usuarios
    usuarios = cargar_datos('Usuarios/Datos_Usuarios.json')

    # Actualizar datos del usuario
    for user in usuarios:
        if user["Nombre"] == usuario:
            # Actualizar datos de compra
            if eleccion in user:
                user[eleccion] += cantidad
            else:
                user[eleccion] = cantidad

    # Guardar los datos actualizados
    guardar_datos(usuarios, 'Usuarios/Datos_Usuarios.json')

    # Registrar la compra en el contador
    with open('Productos_y_Servicios/PyS.json', 'r+') as file:
        datos = json.load(file)
        seccion = None
        if eleccion in datos["Productos"]:
            seccion = "Productos Populares"
        else:
            for categoria, servicios in datos["Servicios"].items():
                if eleccion in servicios:
                    seccion = "Servicios Populares"
                    break

        if seccion:
            if seccion in datos:
                if eleccion in datos[seccion]:
                    datos[seccion][eleccion] += cantidad
                else:
                    datos[seccion][eleccion] = cantidad
            else:
                datos[seccion] = {eleccion: cantidad}

        # Escribir los datos actualizados
        guardar_datos(datos, 'Productos_y_Servicios/PyS.json')
def ofrecer_promocion(nombre_usuario):
    # Cargar los datos de promociones
    promociones = cargar_datos('Productos_y_Servicios/PyS.json')
    tipo_usuario= cargar_datos('Usuarios/Datos_Usuarios.json')
    
    promos={}
    promos=promociones["Promociones"]
    lista = list(tipo_usuario)
    for i in range(len(lista)):
        
        if nombre_usuario == lista[i]["Nombre"]:

            if "Nuevos" == lista[i]["Tipo_usuario"]:
                oferta=(promos["Nuevos"]["PromoInicial"])
                return oferta
            elif "Regulares" == lista[i]["Tipo_usuario"]:
                oferta=(promos["Regulares"]["PromoRegular"])
                return oferta
            elif "Leales" == lista[i]["Tipo_usuario"]:
                oferta=(promos["Leales"]["PromoReales"])
                return oferta
    return "Usuario no registrado"

