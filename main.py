#Importes
from Productos_y_Servicios.modPyS import *
from Usuarios.modUsuarios import *
from Admin import *
import traceback
from datetime import datetime

def log_error(exception):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_message = f"{timestamp}: {str(exception)}\n"
    with open("Errores.txt", "a") as file:
        file.write(error_message)
        traceback.print_exc(file=file)

r = int
try:    
    while r != 0:
        try:  
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
                try: 
                    r=menu_usuario()
                    if r==1:
                        try:  
                            mostrar_productos_servicios()
                            usuario=input("Ingrese su nombre de usuario: ").title()
                            eleccion=input("Ingrese el nombre exacto del producto o servicio que desea adquirir, o si desea salir escriba 'salir': ").title()
                            if eleccion=="salir":
                                break
                            comprar_producto_servicio(usuario, eleccion)
                            print("Compra exitosa")
                            input("Presione enter para ir al menu principal.")
                        except Exception as e:
                            log_error(e)
                    if r==2:
                        try: 
                            nombre = input("Nombre de usuario: ").title()
                            datos=cargar_datos("Usuarios/Datos_Usuarios.json")

                            for i in range(len(datos)):
                                if nombre == datos[i]["Nombre"]:
                                    oferta=ofrecer_promocion(nombre)
                            print(oferta)
                        except Exception as e:
                            log_error(e)
                    if r==3:
                        try:
                            datos="Usuarios/Datos_Usuarios.json"
                            with open(datos, "r") as file:
                                datos_dict = json.load(file)
                            actualizar_usuario(datos_dict)
                            with open(datos, "w") as file:
                                json.dump(datos_dict, file, indent=4)
                        except Exception as e:
                            log_error(e)
                    if r==4:
                        try:
                            datos = "Usuarios/Datos_Usuarios.json"
                            with open(datos, "r") as file:
                                datos_dict = json.load(file)
                            datos_dict = borrar_usuario(datos_dict)
                            with open(datos, "w") as file:
                                json.dump(datos_dict, file, indent=4)
                        except Exception as e:
                            log_error(e)
                except Exception as e:
                    log_error(e)
            elif r==3:
                try:
                    mostrar_productos_servicios()
                    input("Presione enter para volver al menu.")
                except Exception as e:
                    log_error(e)
            elif r==4:
                try:
                    print("/////////////////////////////////////////////////////////////")
                    mostrar_populares()
                    print("/////////////////////////////////////////////////////////////")
                except Exception as e:
                    log_error(e)
            elif r==8:
                try:
                    menu_admin()
                except Exception as e:
                    log_error(e)
            else:
                try:
                    print("Respuesta invalida")
                    r = -1
                except Exception as e:
                    log_error(e)
        except Exception as e:
            log_error(e)
except Exception as e:
    log_error(e)