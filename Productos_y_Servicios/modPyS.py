import json
import traceback
from datetime import datetime
ruta_datos_usuarios = "Usuarios/Datos_Usuarios.json"

def log_error(exception):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_message = f"{timestamp}: {str(exception)}\n"
    with open("Errores.txt", "a") as file:
        file.write(error_message)
        traceback.print_exc(file=file)

def cargar_datos(archivo):
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
        return datos
    except Exception as e:
        log_error(e, "../Errores.txt")
        
def guardar_datos(datos, archivo):
    try:
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)
    except Exception as e:
        log_error(e, "../Errores.txt")

def mostrar_productos_servicios():
    try:
        datos = cargar_datos('Productos_y_Servicios/PyS.json')
        print("Productos Disponibles:")
        for producto, detalles in datos["Productos"].items():
            print(f"{producto}: {detalles['Precio']}")
        print("\nServicios Disponibles:")
        for servicio, precio in datos["Servicios"].items():
            print(f"{servicio}: {precio}")
    except Exception as e:
        log_error(e, "../Errores.txt")

import json

def comprar_producto_servicio(usuario, eleccion, cantidad=1):
    try:
        usuarios = cargar_datos('Usuarios/Datos_Usuarios.json')
        for user in usuarios:
            try:
                if "Nombre" in user and user["Nombre"] == usuario:
                    try:
                        if "Compras" not in user:
                            user["Compras"] = {}
                        if eleccion in user["Compras"]:
                            user["Compras"][eleccion] += cantidad
                        else:
                            user["Compras"][eleccion] = cantidad
                        guardar_datos(usuarios, 'Usuarios/Datos_Usuarios.json')
                        with open('Productos_y_Servicios/PyS.json', 'r+') as file:
                            try:
                                datos = json.load(file)
                                seccion = None
                                if eleccion in datos["Productos"]:
                                    seccion = "Productos Populares"
                                else:
                                    try:
                                        for categoria, servicios in datos["Servicios"].items():
                                            try:
                                                if eleccion in servicios:
                                                    seccion = "Servicios Populares"
                                                    break
                                            except Exception as e:
                                                log_error(e, "../Errores.txt")
                                    except Exception as e:
                                        log_error(e, "../Errores.txt")

                                if seccion:
                                    try:
                                        if seccion in datos:
                                            try:
                                                if eleccion in datos[seccion]:
                                                    datos[seccion][eleccion] += cantidad
                                                else:
                                                    datos[seccion][eleccion] = cantidad
                                            except Exception as e:
                                                log_error(e, "../Errores.txt")
                                        else:
                                            datos[seccion] = {eleccion: cantidad}
                                    except Exception as e:
                                        log_error(e, "../Errores.txt")
                            except Exception as e:
                                log_error(e, "../Errores.txt")

                            guardar_datos(datos, 'Productos_y_Servicios/PyS.json')
                        break
                    except Exception as e:
                        log_error(e, "../Errores.txt")
            except Exception as e:
                log_error(e, "../Errores.txt")
    except Exception as e:
        log_error(e, "../Errores.txt")

def ofrecer_promocion(nombre_usuario):
    try:
        promociones = cargar_datos('Productos_y_Servicios/PyS.json')
        tipo_usuario= cargar_datos('Usuarios/Datos_Usuarios.json')
        promos={}
        promos=promociones["Promociones"]
        lista = list(tipo_usuario)
        for i in range(len(lista)):
            try:
                if nombre_usuario == lista[i]["Nombre"]:
                    try:
                        if "Nuevos" == lista[i]["Tipo_usuario"]:
                            try:
                                oferta=(promos["Nuevos"]["PromoInicial"])
                                return oferta
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                        elif "Regulares" == lista[i]["Tipo_usuario"]:
                            try:
                                oferta=(promos["Regulares"]["PromoRegular"])
                                return oferta
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                        elif "Leales" == lista[i]["Tipo_usuario"]:
                            try:
                                oferta=(promos["Leales"]["PromoReales"])
                                return oferta
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                    except Exception as e:
                        log_error(e, "../Errores.txt")
            except Exception as e:
                log_error(e, "../Errores.txt")
        return "Usuario no registrado"
    except Exception as e:
        log_error(e, "../Errores.txt")

def mostrar_populares():
    try:
        with open("Productos_y_Servicios/PyS.json", "r") as file:
            data = json.load(file)
        print("Productos Populares:")
        productos_populares = data.get("Productos Populares", {})
        for producto, cantidad in productos_populares.items():
            print(f"{producto}: Comprado {cantidad} veces")
        print("\nServicios Populares:")
        servicios_populares = data.get("Servicios Populares", {})
        for servicio, cantidad in servicios_populares.items():
            print(f"{servicio}: Comprado  {cantidad} veces")
    except Exception as e:
        log_error(e, "../Errores.txt")
        
def modificar_productos_servicios_promociones():
    try:
        data = cargar_datos('Productos_y_Servicios/PyS.json')
        while True:
            try:
                print("Seleccione la categoría que desea modificar o agregar:")
                print("1. Productos")
                print("2. Servicios")
                print("3. Promociones")
                print("0. Salir")

                opcion = input("Ingrese su opción: ")

                if opcion == "1":
                    modificar_productos(data)
                elif opcion == "2":
                    modificar_servicios(data)
                elif opcion == "3":
                    modificar_promociones(data)
                elif opcion == "0":
                    print("Saliendo del menú de modificación.")
                    break
                else:
                    print("Opción inválida. Inténtelo de nuevo.")
            except Exception as e:
                log_error(e, "../Errores.txt")
        guardar_datos(data, 'Productos_y_Servicios/PyS.json')
    except Exception as e:
        log_error(e, "../Errores.txt")

def modificar_productos(data):
    try:
        print("Productos disponibles:")
        for producto in data["Productos"]:
            print("-", producto)

        print("Seleccione:")
        print("1. Modificar un producto existente")
        print("2. Agregar un nuevo producto")
        print("3. Eliminar un producto")
        print("0. Volver")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            try:
                producto_a_modificar = input("Ingrese el nombre del producto que desea modificar: ")
                if producto_a_modificar in data["Productos"]:
                    try:
                        print("Características actuales del producto:")
                        print(data["Productos"][producto_a_modificar])
                        almacenamiento = input("Ingrese el Almacenamiento: ")
                        camara = input("Ingrese la resolucion de la camara: ")
                        precio = input("Ingrese el precio: ")
                        data["Productos"][producto_a_modificar]["Almacenamiento: "] = almacenamiento
                        data["Productos"][producto_a_modificar]["Camara: "] = camara
                        data["Productos"][producto_a_modificar]["Precio"] = precio
                        print("Producto modificado exitosamente.")
                    except Exception as e:
                        log_error(e, "../Errores.txt")
                else:
                    print("El producto especificado no existe.")
            except Exception as e:
                log_error(e, "../Errores.txt")

        elif opcion == "2":
            try:
                nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
                almacenamiento = input("Ingrese el almacenamiento del nuevo producto: ")
                camara = input("Ingrese la cámara del nuevo producto: ")
                precio = input("Ingrese el precio del nuevo producto: ")
                data["Productos"][nuevo_producto] = {
                    "Almacenamiento: ": almacenamiento,
                    "Camara: ": camara,
                    "Precio": precio
                }
                print("Nuevo producto agregado exitosamente.")
            except Exception as e:
                log_error(e, "../Errores.txt")

        elif opcion == "3":
            try:
                producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
                if producto_a_eliminar in data["Productos"]:
                    del data["Productos"][producto_a_eliminar]
                    print("Producto eliminado exitosamente.")
                else:
                    print("El producto especificado no existe.")
            except Exception as e:
                log_error(e, "../Errores.txt")
        elif opcion == "0":
            return
        else:
            print("Opción inválida.")
    except Exception as e:
        log_error(e, "../Errores.txt")

def modificar_servicios(data):
    try:
        print("Servicios disponibles:")
        for servicio in data["Servicios"]:
            print("-", servicio)

        print("Seleccione:")
        print("1. Modificar un servicio existente")
        print("2. Agregar un nuevo servicio")
        print("3. Eliminar un servicio")
        print("0. Volver")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            try:
                servicio_a_modificar = input("Ingrese el nombre del servicio que desea modificar: ")
                if servicio_a_modificar in data["Servicios"]:
                    try:
                        print("Precio actual del servicio:")
                        print(data["Servicios"][servicio_a_modificar])
                        precio = input("Ingrese el nuevo precio: ")
                        data["Servicios"][servicio_a_modificar] = precio
                        print("Servicio modificado exitosamente.")
                    except Exception as e:
                        log_error(e, "../Errores.txt")
                else:
                    print("El servicio especificado no existe.")
            except Exception as e:
                log_error(e, "../Errores.txt")
        elif opcion == "2":
            try:
                nuevo_servicio = input("Ingrese el nombre del nuevo servicio: ")
                precio = input("Ingrese el precio del nuevo servicio: ")
                data["Servicios"][nuevo_servicio] = precio
                print("Nuevo servicio agregado exitosamente.")
            except Exception as e:
                log_error(e, "../Errores.txt")
        elif opcion == "3":
            try:
                servicio_a_eliminar = input("Ingrese el nombre del servicio que desea eliminar: ")
                if servicio_a_eliminar in data["Servicios"]:
                    try:
                        del data["Servicios"][servicio_a_eliminar]
                        print("El servicio se eliminara al salir del menu.")
                    except Exception as e:
                        log_error(e, "../Errores.txt")
                else:
                    print("El servicio especificado no existe.")
            except Exception as e:
                log_error(e, "../Errores.txt")
        elif opcion == "0":
            return
        else:
            print("Opción inválida.")
    except Exception as e:
        log_error(e, "../Errores.txt")

def modificar_promociones(data):
    try:
        print("Promociones disponibles:")
        for promocion in data["Promociones"]:
            print("-", promocion)

        print("Seleccione:")
        print("1. Modificar una promoción existente")
        print("2. Agregar una nueva promoción")
        print("3. Eliminar una promoción")
        print("0. Volver")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            promocion_a_modificar = input("Ingrese el nombre de la promoción que desea modificar: ")
        elif opcion == "2":
            nueva_promocion = input("Ingrese el nombre de la nueva promoción: ")
        elif opcion == "3":
            promocion_a_eliminar = input("Ingrese el nombre de la promoción que desea eliminar: ")
        elif opcion == "0":
            return
        else:
            print("Opción inválida.")
    except Exception as e:
        log_error(e, "../Errores.txt")