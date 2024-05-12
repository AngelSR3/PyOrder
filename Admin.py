from Productos_y_Servicios.modPyS import *
from Usuarios.modUsuarios import *
from Usuarios import *
import traceback
from datetime import datetime

def log_error(exception):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_message = f"{timestamp}: {str(exception)}\n"
    with open("Errores.txt", "a") as file:
        file.write(error_message)
        traceback.print_exc(file=file)
def menu_admin():
    try:   
        r=-1
        while r !=0:
            try:
                print("/////////////////////////////////////////////////////////////")
                print("Escriba 1 si desea cambiar la informacion de un usuario.")
                print("Escriba 2 si desea cambiar los productos y servicios.")
                print("Escriba 3 si desea eliminar un usuario.")
                print("Escriba 4 si desea consultar las ventas.")
                print("Escriba 0 si desea salir del programa.")
                r = int(input("->"))
                print("/////////////////////////////////////////////////////////////")
                if r==1:
                    try:
                        datos="Usuarios/Datos_Usuarios.json"
                        with open(datos, "r") as file:
                            datos_dict = json.load(file)
                        actualizar_usuario_admin(datos_dict)
                        with open(datos, "w") as file:
                            json.dump(datos_dict, file, indent=4)
                    except Exception as e:
                        log_error(e)
                elif r==2:
                    try:
                        modificar_productos_servicios_promociones()
                    except Exception as e:
                        log_error(e)
                elif r==3:
                    try:  
                        datos = "Usuarios/Datos_Usuarios.json"
                        with open(datos, "r") as file:
                            datos_dict = json.load(file)
                        datos_dict = borrar_usuario(datos_dict)
                        with open(datos, "w") as file:
                            json.dump(datos_dict, file, indent=4)
                    except Exception as e:
                        log_error(e)
                elif r==4:
                    try:
                        mostrar_ventas()
                    except Exception as e:
                        log_error(e)
            except Exception as e:
                log_error(e)
    except Exception as e:
        log_error(e)