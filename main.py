#Importes
from Productos_y_Servicios.modPyS import *
from Usuarios.modUsuarios import *

r = int
while r != 0:
    print("/////////////////////////////////////////////////////////////")
    print("Bienvenido usuario.")
    print("Escriba 1 si desea registrarse como nuevo usuario.")
    print("Escriba 2 si desea acceder al menu de usuarios (Usuarios existentes o Administradores(Escribir 8)).")
    print("Escriba 3 si desea consultar el catálogo de productos y servicios.")
    print("Escriba 4 si desea consultar los productos y servicios mas populares.")
    print("Escriba 0 si desea salir del programa.")
    print("/////////////////////////////////////////////////////////////")
    r = int(input("->"))
    if r == 1:
        Usuario_Nuevo()
    elif r == 2:
        r=menu_usuario()
        if r==1:
            mostrar_productos_servicios()
            usuario=input("Ingrese su nombre de usuario: ").title()
            eleccion=input("Ingrese el nombre exacto del producto o servicio que desea adquirir, o si desea salir escriba 'salir': ").title()
            if eleccion=="salir":
                break
            comprar_producto_servicio(usuario, eleccion)
            print("Compra exitosa")
            input("Presione enter para ir al menu principal.")
        if r==2:
            nombre = input("Nombre de usuario: ").title()
            datos=cargar_datos("Usuarios/Datos_Usuarios.json")

            for i in range(len(datos)):
                if nombre == datos[i]["Nombre"]:
                    oferta=ofrecer_promocion(nombre)
            print(oferta)
        if r==3:
            datos="Usuarios/Datos_Usuarios.json"
            actualizar_usuario(datos)
    else:
        print("Respuesta invalida")
        r = int(0)  