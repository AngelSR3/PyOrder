import json

def guardar_datos_usuarios(usuarios):
    with open("Usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)

def cargar_datos_usuarios():
    try:
        with open("Usuarios.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def agregar_usuario():
    usuario = {}
    print("/////////////////////////////////////////////////////////////")
    usuario["Nombre"] = input("Primer nombre y primer apellido: ").title()
    usuario["Direccion"] = input("Direccion: ").title()
    usuario["Contacto"] = input("Telefono de contacto: ")

    return usuario

def Usuario_Nuevo():
    usuarios = cargar_datos_usuarios()

    while True:
        usuario = agregar_usuario()
        usuarios.append(usuario)

        guardar_datos_usuarios(usuarios)

        break

    print("Registrado correctamente.")
    print("/////////////////////////////////////////////////////////////")
    r=int
    while r!=0:
        print("Escriba 1 si desea adquirir un servicio.")
        print("Escriba 2 si desea comprar un producto")
        print("Escriba 3 si desea consultar servicios y promociones sugeridas.")
        print("Escriba 4 si desea eliminar su cuenta.")
        print("Escriba 5 si desea consultar los productos y servicios mas populares.")
        print("Escriba 0 si desea cerrar sesion y volver al menu principla.")
        r=int(input())