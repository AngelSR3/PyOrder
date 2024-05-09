r=int

while r!=0:
    print("/////////////////////////////////////////////////////////////")
    print("Bienvenido usuario.")
    print("Escriba 1 si desea registrarse como nuevo usuario.")
    print("Escriba 2 si desea iniciar sesion (Usuarios existentes o Administradores(Admin)).")
    print("Escriba 3 si desea eliminar un usuario existente.")
    print("Escriba 4 si desea consultar el catalogo de productos")
    print("Escriba 5 si desea consultar los productos y servicios mas populares.")
    print("Escriba 0 si desea salir del programa.")
    print("/////////////////////////////////////////////////////////////")
    r=int(input("->"))
    if r==1:
        from Usuarios.modUsuarios import *
        Usuario_Nuevo()