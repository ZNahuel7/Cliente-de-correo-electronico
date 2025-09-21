# Cliente de correo electronico

Este proyecto consite en desarrollar un sistema para conformar la estructura de un sistema de correo electrónico aplicando principios sólidos de programación orientada a objetos. El lenguaje de programación utilizado fue Python. 

Esta primer entrega se enfocó en establecer una base sólida con las clases fundamentales requeridas y las operaciones esenciales de gestión de usuarios, mensajes y carpetas, con un enfoque en encapsulamiento.

## Estructura del proyecto

En esta primera etapa, se hace entrega del archivo correo.py, que contiene las clases principales del sistema. Se incluye también el readme correspondiente. Del mismo modo se adjunta el link para acceder a la carpeta compartida donde se incluye el diagrama UML del presente proyecto en formato .png:

https://drive.google.com/file/d/13Ce4H6d9us4s-LEA_bBzaMHMpQPivK5k/view?usp=sharing

En proximas entregas se planea confeccionar el archivo main.py para hacer muestra del funcionamiento e interrelación de las clases creadas.
```
proyecto/
├── correo.py          # Clases principales del sistema
├── main.py            # Punto de entrada del programa
├── README.md          # Instrucciones del proyecto
```
## Clases que se implementaron

### Clase Mensaje

Representa un mensaje de correo electrónico con los siguientes atributos:

- `emisor`: Usuario que envía el mensaje
- `receptor`: Usuario que recibe el mensaje
- `asunto`: Asunto del mensaje
- `cuerpo`: Contenido principal del mensaje

### Clase Usuario

Representa a un usuario del sistema con:

- `nombre`: Nombre del usuario
- `correo`: Dirección de correo electrónico
- `buzon`_entrada: Lista de mensajes recibidos

### Clase Servidor
Gestiona el sistema central con:

- `usuarios`: Lista de usuarios registrados
- Funciones de registro y envío de mensajes

### Clase Carpeta

- `nombre`: Identificador de la carpeta
- `mensajes_en_carpeta`: Colección de mensajes almacenados

### Requisitos
- Python 3.x
- No se requieren dependencias externas

### Funcionalidades que fueron implementadas
- Registro de usuarios en el servidor
- Envío y recepción de mensajes entre usuarios
- Organización de mensajes en carpetas personalizadas
- Visualización de contenido de buzones y carpetas
- Modificación controlada de mensajes existentes

### Ejecución
El archivo principal para ejecutar el programa aun se encuentra en desarrollo

### Ejemplo de uso
Se confeccionará el ejemplo de uso una vez que el archivo main.py y la interfaz web termine de desarrollarse.

### Autores 
- Zárate, Ezequiel
- Zárate, Nahuel

### Licencia
Este proyecto es de uso académico y educativo para la materia Estructura de Datos.

### Notas
- Se implementó un encapsulamiento estricto con atributos privados y métodos de acceso controlado.
- El diseño modular permitirá la fácil extensión para futuras funcionalidades
- Se espera añadir más clases y métodos para desarrollar un programa completo y funcional
- Se espera que la interfaz se desempeñe bajo un sitio web.
- Queda pendiente para la proxima entrega el testing de las diferentes clases para comprobar el correcto funcionamiento del código.
- Se han planteados ideas para implementar a futuro:
  · Sistema de filtros automáticos
  · Motor de búsqueda eficiente
  · Persistencia en archivos
