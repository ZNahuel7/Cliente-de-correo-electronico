# Cliente de correo electronico

Este proyecto consiste en desarrollar un sistema con la estructura de un correo electronico aplicando principios de programación orientada a objetos. El lenguaje utilizado es Python.

## Segunda entrega: Estructuras de Datos y Recursividad

En esta segunda entrega se implementó la gestión de carpetas y subcarpetas como un árbol recursivo, permitiendo:
- Crear carpetas y subcarpetas de manera ilimitada.
- Mover mensajes entre carpetas y subcarpetas.
- Realizar búsquedas recursivas de mensajes por asunto o remitente.
- Analizar la eficiencia de las operaciones principales.
También se agregaron ejemplos de uso en el archivo `main.py`.

## Estructura del proyecto

En esta segunda etapa, se hace entrega del conjunto de archivos corrspondientes al proyecto. Se incluye el readme correspondiente, asi como la carpeta docs, donde se encuentra la documentacion y diagramas confeccionados.

```
proyecto/
├── carpeta.py             # Clase Carpeta
├── mensaje.py             # Clase Mensaje
├── usuario.py             # Clase Usuario
├── servidor.py            # Clase ServidorCorreo
├── main.py                # Ejemplo de uso y pruebas
├── docs/
│   └── readme.md          # Instrucciones del proyecto
    └── informe.txt        # Documentación de los nuevos cambios realizados
    └── DiagramaUML.png    # Diagrama de clases     
```
## Clases principales

### Clase Mensaje
Representa un mensaje de correo electrónico. Se conforma por:
- `emisor`: usuario que envía el mensaje
- `receptor`: usuario que recibe el mensaje
- `asunto`: asunto del mensaje
- `cuerpo`: contenido principal del mensaje

### Clase Carpeta (Árbol de carpetas)
Permite organizar mensajes en carpetas y subcarpetas. Esta conformada por:
- `nombre`: nombre de la carpeta
- `mensajes`: lista de mensajes en la carpeta
- `subcarpetas`: lista de subcarpetas
- Métodos para agregar subcarpetas, mover mensajes y buscar recursivamente

### Clase Usuario
Representa a un usuario del sistema. Se conforma por:
- `nombre`: Nombre del usuario
- `correo`: Dirección de correo electrónico
- `carpetas`: Lista de carpetas principales (que tambien pueden tener subcarpetas)
- Métodos para recibir mensajes, mover mensajes y buscar recursivamente

### Clase ServidorCorreo
Gestiona el sistema central. Se conforma por:
- Funciones de envío de mensajes
- Listado de mensajes
- Mover mensajes entre carpetas
- Búsqueda recursiva de mensajes

## Interacción entre clases
- El `ServidorCorreo` se encarga de crear y entregar los mensajes a los usuarios.
- Los usuarios reciben los mensajes a traves de su bandeja de entrada (Carpeta).
- Los mensajes contienen referencias a los usuarios que los envían y reciben.

### Requisitos
- Python 3.x
- No se requieren dependencias externas

## Funcionalidades implementadas
- Registro de usuarios en el servidor
- Envío y recepción de mensajes entre usuarios
- Organización de mensajes en carpetas y subcarpetas
- Mover mensajes entre carpetas y subcarpetas
- Búsqueda recursiva de mensajes por asunto o remitente
- Visualización de contenido de buzones y carpetas
- Modificación controlada de mensajes existentes
- Todos los atributos de las clases son privados y se accede a ellos mediante métodos, cumpliendo con el principio de encapsulamiento.
- Cada clase está en su propio archivo, lo que mejora la modularidad y la organización del código.

## Ejecución
Ejecuta el archivo `main.py` para ver ejemplos de uso y pruebas de las funcionalidades.

## Ejemplo de uso
En `main.py` se muestran ejemplos de:
- Envío de mensajes
- Creación de subcarpetas
- Movimiento de mensajes entre carpetas
- Búsqueda recursiva de mensajes

## Autores
- Zárate, Ezequiel
- Zárate, Nahuel

## Licencia
Este proyecto es de uso académico y educativo para la materia Estructura de Datos.

## Notas
- Se implementó un encapsulamiento estricto con atributos privados y métodos de acceso controlado.
- El diseño modular permite la facil extensión para futuras funcionalidades.
- El arbol de carpetas permite organizar y buscar mensajes de forma eficiente y flexible.
