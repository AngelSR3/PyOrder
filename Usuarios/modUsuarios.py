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

def guardar_datos_usuarios(usuarios):
    with open(ruta_datos_usuarios, "w") as archivo:
        json.dump(usuarios, archivo)

def cargar_datos_usuarios():
    try:
        with open(ruta_datos_usuarios, "r") as archivo:
            return json.load(archivo)
    except Exception as e:
        log_error(e, "../Errores.txt")

def agregar_usuario():
    try: 
        usuario = {}
        print("/////////////////////////////////////////////////////////////")
        usuario["Nombre"] = input("Primer nombre: ").title()
        usuario["Direccion"] = input("Direccion: ").title()
        usuario["Contacto"] = input("Telefono de contacto: ")
        usuario["Id"] = input("Documento de ID: ")
        usuario["Tipo_usuario"]="Nuevos"
        usuario["Compras"] = {}
        return usuario
    except Exception as e:
        log_error(e, "../Errores.txt")

def Usuario_Nuevo():
    try:
        usuarios = cargar_datos_usuarios()

        if not usuarios:
            usuarios = []

        while True:
            usuario = agregar_usuario()
            usuarios.append(usuario)

            guardar_datos_usuarios(usuarios)

            break
        print("Registrado correctamente.")
        input("Presione enter para volver al menu principal.")
        print("/////////////////////////////////////////////////////////////////////////////")
        r = -1
    except Exception as e:
        log_error(e, "../Errores.txt")
        
def menu_usuario():
    try: 
        r=int
        while r != 0:
            print("/////////////////////////////////////////////////////////////////////////////")
            print("Escriba 1 si desea comprar un producto o adquirir un servicio.")
            print("Escriba 2 si desea consultar servicios y promociones sugeridas.")
            print("Escriba 3 si desea actualizar la informacion de su cuenta.")
            print("Escriba 4 si desea eliminar su cuenta.")
            print("Escriba 0 si desea cerrar sesion y volver al menu principal.")
            r = int(input("->"))
            print("/////////////////////////////////////////////////////////////////////////////")
            if r == 1:
                return r
            elif r == 2:
                return r
            elif r == 3:
                return r
            elif r == 4:
                return r
            elif r == 0:
                r=0
                return r
            else:
                try:
                    print("Respuesta invalida")
                    input("Presione enter para volver al menu principal.")
                except Exception as e:
                    log_error(e, "../Errores.txt")
        return r
    except Exception as e:
        log_error(e, "../Errores.txt")
def actualizar_usuario(datos: list):
    try:
        id = input("Ingrese el documento del cliente a reemplazar: ")
        for usuario in datos:
            try:
                if "Id" in usuario and usuario["Id"] == id:
                    try:
                        print("Usuario encontrado:")
                        print("Nombre:", usuario["Nombre"])
                        print("Documento:", usuario["Id"], (" Esto no se puede cambiar"))
                        print("Dirección:", usuario["Direccion"])
                        print("Contacto:", usuario["Contacto"])
                        print("Tipo de usuario:", usuario["Tipo_usuario"], " (Esto solo puede ser modificado por Admins)")
                        while True:
                            try:
                                print("¿Qué te gustaría cambiar?")
                                print("(1) para modificar el nombre")
                                print("(2) para modificar la dirección")
                                print("(3) para modificar el contacto")
                                print("(0) para salir")
                                opc = input("Ingrese la opción: ")

                                if opc == "1":
                                    try:
                                        usuario["Nombre"] = input("Ingrese el nuevo nombre: ")
                                        print("Se guardó con éxito")
                                        print("/////////////////////////////////////////////////////////////")
                                    except Exception as e:
                                        log_error(e, "../Errores.txt")
                                elif opc == "2":
                                    try:
                                        usuario["Direccion"] = input("Ingrese la nueva dirección: ")
                                        print("Se guardó con éxito")
                                        print("/////////////////////////////////////////////////////////////")
                                    except Exception as e:
                                        log_error(e, "../Errores.txt")
                                elif opc == "3":
                                    try:
                                        usuario["Contacto"] = input("Ingrese el nuevo teléfono: ")
                                        print("Se guardó con éxito")
                                        print("/////////////////////////////////////////////////////////////")
                                    except Exception as e:
                                        log_error(e, "../Errores.txt")
                                elif opc == "0":
                                    try:
                                        print("Su información se guardó correctamente.")
                                        print("Nombre:", usuario["Nombre"])
                                        print("Dirección:", usuario["Direccion"])
                                        print("Contacto:", usuario["Contacto"])
                                        print("Tipo de usuario:", usuario["Tipo_usuario"], " (Esto solo puede ser modificado por Admins)")
                                        print("Documento:", usuario["Id"])
                                        input("Presione enter para volver al menú principal.")
                                        break
                                    except Exception as e:
                                        log_error(e, "../Errores.txt")
                                else:
                                    print("Respuesta inválida.")
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                        break
                    except Exception as e:
                        log_error(e, "../Errores.txt")
            except Exception as e:
                log_error(e, "../Errores.txt")
        else:
            print("Usuario no encontrado/registrado.")
            input("Presione enter para volver al menú principal.")
        return datos
    except Exception as e:
        log_error(e, "../Errores.txt")
        
def actualizar_usuario_admin(datos: list):
    try:
        while True:
            try:
                id = input("Ingrese el documento del cliente a reemplazar (o escriba 0 para salir): ")
                if id == "0":
                    print("Saliendo del menú de actualización.")
                    return datos
                
                for usuario in datos:
                    try:
                        if "Id" in usuario and usuario["Id"] == id:
                            try:
                                print("Usuario encontrado:")
                                print("Nombre:", usuario["Nombre"])
                                print("Documento:", usuario["Id"], "Esto no se puede cambiar")
                                print("Dirección:", usuario["Direccion"])
                                print("Contacto:", usuario["Contacto"])
                                print("Tipo de usuario:", usuario["Tipo_usuario"], "(Esto solo puede ser modificado por Admins)")
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                            try:
                                while True:
                                    try:
                                        print("/////////////////////////////////////////////////////////////")
                                        print("¿Qué te gustaría cambiar?")
                                        print("(1) para modificar el nombre")
                                        print("(2) para modificar la dirección")
                                        print("(3) para modificar el contacto")
                                        print("(4) para modificar el tipo de usuario")
                                        print("(0) para salir")
                                        opc = input("Ingrese la opción: ")
                                    except Exception as e:
                                        log_error(e, "../Errores.txt")
                                    if opc == "1":
                                        try:
                                            usuario["Nombre"] = input("Ingrese el nuevo nombre: ").title()
                                            print("Se guardó con éxito")
                                        except Exception as e:
                                            log_error(e, "../Errores.txt")
                                    elif opc == "2":
                                        try:
                                            usuario["Direccion"] = input("Ingrese la nueva dirección: ")
                                            print("Se guardó con éxito")
                                        except Exception as e:
                                            log_error(e, "../Errores.txt")
                                    elif opc == "3":
                                        try:
                                            usuario["Contacto"] = input("Ingrese el nuevo teléfono: ")
                                            print("Se guardó con éxito")
                                        except Exception as e:
                                            log_error(e, "../Errores.txt")
                                    elif opc == "4":
                                        try:
                                            usuario["Tipo_usuario"] = input("Ingrese el tipo de este usuario (Nuevos)(Regulares)(Leales): ").title()
                                            if usuario["Tipo_usuario"] not in ["Nuevos", "Regulares", "Leales"]:
                                                print("Respuesta inválida")
                                                break
                                            print("Se guardó con éxito")
                                        except Exception as e:
                                            log_error(e, "../Errores.txt")
                                    elif opc == "0":
                                        try:
                                            print("Su información se guardó correctamente.")
                                            print("Nombre:", usuario["Nombre"])
                                            print("Dirección:", usuario["Direccion"])
                                            print("Contacto:", usuario["Contacto"])
                                            print("Tipo de usuario:", usuario["Tipo_usuario"], "(Esto solo puede ser modificado por Admins)")
                                            print("Documento:", usuario["Id"])
                                            input("Presione enter para continuar.")
                                            break
                                        except Exception as e:
                                            log_error(e, "../Errores.txt")
                                    else:
                                        print("Respuesta inválida.")
                                break
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                    except Exception as e:
                        log_error(e, "../Errores.txt")
                else:
                    print("Usuario no encontrado/registrado.")
            except Exception as e:
                log_error(e, "../Errores.txt")
        return datos
    except Exception as e:
        log_error(e, "../Errores.txt")



def borrar_usuario(datos: list):
    try:
        id = input("Ingrese el documento del cliente a borrar: ")
        for usuario in datos:
            try:
                if usuario and "Id" in usuario and usuario["Id"] == id:
                    try:
                        print("/////////////////////////////////////////////////////////////")
                        print("Usuario encontrado:")
                        print("Nombre:", usuario["Nombre"])
                        if "Id" in usuario:
                            print("Documento:", usuario["Id"])
                        else:
                            print("El usuario no tiene un documento asociado.")
                        print("Dirección:", usuario.get("Direccion", "No disponible"))
                        print("Contacto:", usuario.get("Contacto", "No disponible"))
                        print("Tipo de usuario:", usuario.get("Tipo_usuario", "No disponible"))

                        confirmacion = input("¿Está seguro de que desea eliminar este usuario? Escriba 1 para confirmar y 2 para cancelar: ")
                        if confirmacion == "1":
                            try:
                                datos.remove(usuario)
                                print("Usuario eliminado con éxito")
                                return datos
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                        elif confirmacion == "2":
                            try:
                                input("Cancelado. Presione enter para volver al menú principal.")
                                print("/////////////////////////////////////////////////////////////")
                                return datos
                            except Exception as e:
                                log_error(e, "../Errores.txt")
                        else:
                            print("Respuesta inválida")
                    except Exception as e:
                        log_error(e, "../Errores.txt")
            except Exception as e:
                log_error(e, "../Errores.txt")
        print("Usuario no encontrado.")
        input("Presione enter para volver.")
        return datos
    except Exception as e:
        log_error(e, "../Errores.txt")

def actualizar_datos_usuario(usuario, datos_nuevos):
    try:
        for key, value in datos_nuevos.items():
            usuario[key] = value
    except Exception as e:
        log_error(e, "../Errores.txt")

def registrar_venta(usuario, producto, cantidad=1):
    try:
        if "Compras" not in usuario:
            usuario["Compras"] = {}
        if producto in usuario["Compras"]:
            usuario["Compras"][producto] += cantidad
        else:
            usuario["Compras"][producto] = cantidad
    except Exception as e:
        log_error(e, "../Errores.txt")

def obtener_usuario_mas_compras(usuarios):
    try:
        max_compras = 0
        usuario_mas_compras = None
        for usuario in usuarios:
            try:
                total_compras = 0  # Inicializa el total de compras para cada usuario
                if "Compras" in usuario and usuario["Compras"]:
                    try:
                        for cantidad in usuario["Compras"].values():  # Suma las compras de cada usuario
                            total_compras += cantidad
                        if total_compras > max_compras:
                            max_compras = total_compras
                            usuario_mas_compras = usuario["Nombre"]
                    except Exception as e:
                        log_error(e, "../Errores.txt")
            except Exception as e:
                log_error(e, "../Errores.txt")
        return usuario_mas_compras
    except Exception as e:
        log_error(e, "../Errores.txt")

def mostrar_ventas():
    try:
        usuarios = cargar_datos_usuarios()
        for usuario in usuarios:
            try:
                print("/////////////////////////////////////////////////////////////")
                print("Nombre del usuario:", usuario["Nombre"])
                if "Compras" in usuario:
                    print("Ventas realizadas:")
                    for producto, cantidad in usuario["Compras"].items():
                        print(f"Producto: {producto}, Cantidad: {cantidad}")
                else:
                    print("Este usuario no ha realizado ninguna compra.")
            except Exception as e:
                log_error(e, "../Errores.txt")
        print("/////////////////////////////////////////////////////////////")
        print(obtener_usuario_mas_compras(usuarios))
    except Exception as e:
        log_error(e, "../Errores.txt")