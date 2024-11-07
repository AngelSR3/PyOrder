# Pyorder

## Descripción

PyOrder es un sistema de gestión que permite a los usuarios registrarse, acceder a un catálogo de productos y servicios, realizar compras y recibir promociones. Los administradores tienen acceso a funcionalidades adicionales, como la gestión de usuarios, productos y servicios, y la consulta de ventas. El sistema está dividido en varios módulos para una fácil extensión y mantenimiento.

## Características

- **Usuarios**: Los usuarios pueden registrarse, acceder al menú para comprar productos, recibir promociones y administrar sus datos.
- **Administradores**: Los administradores pueden modificar los productos y servicios, cambiar la información de los usuarios, eliminar usuarios y consultar las ventas.
- **Productos y Servicios**: Se presenta un catálogo de productos y servicios con la posibilidad de adquirirlos y ver los más populares.
- **Errores**: El sistema maneja errores y los registra en un archivo `Errores.txt` para su posterior revisión.

## Estructura del Proyecto

### Archivos Principales

- **`main.py`**: Archivo principal que gestiona la interacción con el usuario, donde se encuentran las opciones para registrarse, acceder al menú de usuario, consultar productos y más.
- **`Admin.py`**: Módulo que gestiona las funciones administrativas, como la modificación de usuarios, productos y la consulta de ventas.
- **`modUsuarios.py`**: Módulo encargado de la gestión de los datos de los usuarios, registro y actualizaciones.
- **`modPyS.py`**: Módulo que gestiona los productos y servicios disponibles, incluyendo su catálogo y promociones.
- **`Errores.txt`**: Archivo donde se registran los errores ocurridos durante la ejecución del programa.

### Funcionalidades

#### Para los usuarios:

1. **Registro**: Los usuarios pueden registrarse para ser parte del sistema.
2. **Consulta de productos y servicios**: Los usuarios pueden ver el catálogo de productos y servicios disponibles.
3. **Compra**: Los usuarios pueden adquirir productos o servicios.
4. **Promociones**: Los usuarios pueden recibir promociones personalizadas.
5. **Gestión de usuario**: Los usuarios pueden actualizar o eliminar su cuenta.

#### Para los administradores:

1. **Modificar usuarios**: Los administradores pueden actualizar la información de los usuarios.
2. **Modificar productos y servicios**: Los administradores pueden añadir, editar o eliminar productos y servicios.
3. **Eliminar usuarios**: Los administradores tienen la capacidad de eliminar usuarios del sistema.
4. **Consultar ventas**: Los administradores pueden ver un registro de las ventas realizadas.

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/AngelSR3/PyOrder.git
   ```
2. **Instalar dependencias**:
   Asegúrate de tener Python instalado. Si es necesario, instala las dependencias del proyecto.

3. **Ejecutar el sistema**:
   
   En la terminal, navega a la carpeta del proyecto y ejecuta el archivo principal:

   ```bash
   python main.py
   ```
## Manejo de Errores

El sistema registra todos los errores en un archivo de log `Errores.txt`. Cualquier excepción que ocurra será registrada con un timestamp para su revisión posterior.

## Estructura de Archivos

- **`main.py`**: Control principal del sistema, interacción con el usuario.
- **`Admin.py`**: Gestión de funciones administrativas.
- **`modUsuarios.py`**: Módulo que gestiona las acciones relacionadas con los usuarios.
- **`modPyS.py`**: Módulo que gestiona los productos y servicios disponibles.
- **`Errores.txt`**: Archivo de log que almacena los errores registrados.

## Contacto

- **Email**: angelduvan1016@gmail.com
- **GitHub**: https://github.com/AngelSR3
- **LinkedIn**: https://www.linkedin.com/in/angelsr3

## ¡Gracias por usar PyOrder! 🎉
