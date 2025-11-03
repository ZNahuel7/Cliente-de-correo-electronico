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

En esta tercer etapa, se hace entrega del conjunto de archivos correspondientes al proyecto. Se incluye el readme correspondiente, asi como la carpeta docs, donde se encuentra la documentacion y diagramas confeccionados.
```
proyecto/
├── carpeta.py             # Clase Carpeta
├── mensaje.py             # Clase Mensaje
├── usuario.py             # Clase Usuario
├── servidor.py            # Clase ServidorCorreo
├── main.py                # Ejemplo de uso y pruebas
├── readme.md              # Instrucciones del proyecto
├── docs/
│   └── Diagrama-UML.png   # Diagrama de clases (tercer entrega)
    └── informe.txt        # Documentación de los nuevos cambios realizados
    └── DiagramaUML.png    # Diagrama de clases(segunda entrega)
    └── UML.png            # Diagrama de clases (primer entrega)
```
## Clases principales

**Clase Mensaje**
Representa un mensaje de correo electrónico. Se conforma por:
- `emisor`: usuario que envía el mensaje
- `receptor`: usuario que recibe el mensaje
- `asunto`: asunto del mensaje
- `cuerpo`: contenido principal del mensaje

**Clase Carpeta (Árbol de carpetas)**
Permite organizar mensajes en carpetas y subcarpetas. Esta conformada por:
- `nombre`: nombre de la carpeta
- `mensajes`: lista de mensajes en la carpeta
- `subcarpetas`: lista de subcarpetas
- Métodos para agregar subcarpetas, mover mensajes y buscar recursivamente

**Clase Usuario**
Representa a un usuario del sistema. Se conforma por:
- `nombre`: Nombre del usuario
- `correo`: Dirección de correo electrónico
- `carpetas`: Lista de carpetas principales (que tambien pueden tener subcarpetas)
- Métodos para recibir mensajes, mover mensajes y buscar recursivamente

**Clase ServidorCorreo**
Gestiona el sistema central. Se conforma por:
- Funciones de envío de mensajes
- Listado de mensajes
- Mover mensajes entre carpetas
- Búsqueda recursiva de mensajes

## Interacción entre clases
- El `ServidorCorreo` se encarga de crear y entregar los mensajes a los usuarios.
- Los usuarios reciben los mensajes a traves de su bandeja de entrada (Carpeta).
- Los mensajes contienen referencias a los usuarios que los envían y reciben.


## Análisis de Complejidad Algorítmica

### Operaciones Principales

**Agregar Mensaje**
- Complejidad: O(1) para mensajes normales, O(log n) para mensajes urgentes
- Justificación: 
  - Los mensajes normales se agregan al final de una lista simple, lo que es una operación de tiempo constante
  - Los mensajes urgentes requieren mantener un orden, usando inserción ordenada que tiene complejidad logarítmica
  - Los filtros automáticos pueden redirigir el mensaje, pero esto no aumenta la complejidad total

**Buscar Mensajes**
- Complejidad: O(m * p) donde m es el número total de mensajes y p es la profundidad máxima del árbol
- Justificación:
  - Se debe examinar cada mensaje en cada nivel del árbol de carpetas
  - La búsqueda es recursiva, bajando por todas las subcarpetas
  - En el peor caso, debemos visitar todas las carpetas y revisar todos los mensajes

**Mover Mensaje**
- Complejidad: O(p) donde p es la profundidad del árbol de carpetas
- Justificación:
  - Debemos encontrar la carpeta que contiene el mensaje
  - En el peor caso, tenemos que bajar hasta el nivel más profundo del árbol
  - La operación de remover y agregar el mensaje es O(1)

**Aplicar Filtros**
- Complejidad: O(m) donde m es el número de mensajes en la carpeta
- Justificación:
  - Cada mensaje debe ser evaluado contra todos los filtros existentes
  - El número de filtros es típicamente pequeño y constante
  - Las operaciones de comparación de strings son O(1) en promedio

### Estructuras de Datos Utilizadas

**Árbol de Carpetas**
- Implementación: Árbol general donde cada nodo (carpeta) puede tener múltiples hijos
- Ventajas:
  - Representa naturalmente la jerarquía de carpetas
  - Permite búsquedas recursivas eficientes
  - Facilita la organización de mensajes en subcarpetas

**Cola de Prioridad para Mensajes Urgentes**
- Implementación: Lista ordenada por prioridad
- Ventajas:
  - Acceso rápido a mensajes urgentes
  - Mantiene el orden de llegada dentro de la misma prioridad
  - Implementación simple y eficiente para la escala esperada

**Diccionario de Filtros**
- Implementación: Diccionario con reglas de filtrado
- Ventajas:
  - Acceso O(1) a las reglas de filtrado
  - Fácil actualización y eliminación de filtros
  - Aplicación eficiente de múltiples reglas

### Casos Borde y su Manejo

**Carpetas Vacías**
- Manejo: Retorna lista vacía en búsquedas
- No causa errores en operaciones de movimiento

**Mensajes Inexistentes**
- Manejo: Retorna False al intentar mover
- No afecta el estado del sistema

**Filtros Inválidos**
- Manejo: Ignora campos de filtro inválidos
- Mantiene el comportamiento predeterminado

**Profundidad Extrema**
- La recursividad está limitada por la profundidad máxima del árbol
- Manejo gracioso de estructuras profundamente anidadas

## Requisitos
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
- Todos los atributos de las clases son privados y se accede a ellos mediante métodos, cumpliendo con el principio de encapsulamiento
- Cada clase está en su propio archivo, lo que mejora la modularidad y la organización del código
- Filtros automáticos para organizar mensajes según reglas definidas por el usuario
- Creación y eliminación dinámica de filtros por asunto, remitente o contenido
- Sistema de prioridades para mensajes urgentes
- Listado de mensajes con opción de mostrar solo urgentes
- Visualización recursiva de mensajes en carpetas y subcarpetas
- Mantenimiento automático del orden en mensajes urgentes

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
