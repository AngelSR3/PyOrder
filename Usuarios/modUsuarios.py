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
    usuario["Tipo_usuario"]="Leal"
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
    print("/////////////////////////////////////////////////////////////////////////////")
    r = -1
def menu_usuario():
    r=int
    while r != 0:
        print("/////////////////////////////////////////////////////////////////////////////")
        print("Escriba 1 si desea comprar un producto o adquirir un servicio.")
        print("Escriba 2 si desea consultar servicios y promociones sugeridas.")
        print("Escriba 3 si desea ver la informacion de su cuenta.")
        print("Escriba 4 si desea eliminar su cuenta.")
        print("Escriba 5 si desea consultar los productos y servicios mas populares.")
        print("Escriba 0 si desea cerrar sesion y volver al menu principla.")
        r = int(input("->"))
        print("/////////////////////////////////////////////////////////////////////////////")
        if r == 1:
            return r
        elif r == 2:
            return r
        else:
            print("Respuesta invalida")
    return r