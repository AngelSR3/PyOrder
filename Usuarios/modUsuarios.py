import json
ruta_datos_usuarios = "Usuarios/Datos_Usuarios.json"

def guardar_datos_usuarios(usuarios):
    with open(ruta_datos_usuarios, "w") as archivo:
        json.dump(usuarios, archivo)

def cargar_datos_usuarios():
    try:
        with open(ruta_datos_usuarios, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def agregar_usuario():
    usuario = {}
    print("/////////////////////////////////////////////////////////////")
    usuario["Nombre"] = input("Primer nombre: ").title()
    usuario["Direccion"] = input("Direccion: ").title()
    usuario["Contacto"] = input("Telefono de contacto: ")
    usuario["Id"] = input("Documento de ID: ")
    usuario["Tipo_usuario"]="Nuevos"
    return usuario

def Usuario_Nuevo():
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
def menu_usuario():
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
        else:
            print("Respuesta invalida")
    return r
def actualizar_usuario(datos:dict):
    id =input("Ingrese el documento del cliente a remplazar: ")
    for i in range(len(datos)):
        if datos[i]["Id"]== id:


            while True:
                print("¿que te gustaria cambiar?")
                print("(1) para modificar el nombre: ")
                print("(2) para modificar el documento: ")
                print("(3) para modificar la direccion: ")
                print("(4) para modificar el contacto: ")
                print("(0) para salir ")
                opc=input("ingrese la opcion: ")




                if opc=="1":
                    datos[i]["Nombre"]= input("ingrese el nuevo nombre: ")
                    print("se guardo con exito")
                    print("/////////////////////////////////////////////////////////////")
                elif opc== "2":
                    datos[i]["Id"]=input("ingrese el nuevo documento: ")
                    print("se guardo con exito")
                    print("/////////////////////////////////////////////////////////////")
                elif opc=="3":
                    datos[i]["Direccion"]= input("ingrese la nueva direccion: ")
                    print("se guardo con exito")
                    print("/////////////////////////////////////////////////////////////")
                elif opc=="4":
                    datos[i]["Contacto"]= input("ingrese el nuevo telefono: ")
                    print("se guardo con exito")
                    print("/////////////////////////////////////////////////////////////")
                elif opc=="0":
                    break
            break
    return datos