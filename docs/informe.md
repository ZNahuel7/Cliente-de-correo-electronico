## 09-10
### Informe
Se realizaron diferentes correcciones de acuerdo a la devolución recibida y a las cosignas del proyecto. Algunas de estas fueron:

Implementar los métodos de la interfaz básica:
- enviar_mensaje(remitente, destinatario, asunto, cuerpo)
- recibir_mensaje(usuario)
- listar_mensajes(carpeta)

Modularizar el proyecto siguiendo la estructura recomendada:
- usuario.py → clase Usuario
- mensaje.py → clase Mensaje
- carpeta.py → clase Carpeta
- servidor.py → clase ServidorCorreo
- main.py → archivo principal para pruebas
- docs/ → carpeta para diagramas y documentación

## 11-10
### Informe
Se realizaron diferentes cambios para cumplir con la consigna de esta segunda entrega. Algunas de estas fueron:
I. Se modificó la clase Carpeta para que sea recursiva:
- Ahora una carpeta puede tener subcarpetas (estructura de árbol general).
- Se agregaron métodos para agregar subcarpetas y obtener la lista de subcarpetas.
II. Se agregaron métodos para mover mensajes entre carpetas:
- Se implementó un método mover_mensaje que permite buscar y mover un mensaje de una carpeta (o subcarpeta) a otra.
III. Se agregó búsqueda recursiva de mensajes:
- Se implementó el método buscar_mensajes, que permite buscar mensajes por asunto o remitente recorriendo todas las subcarpetas de manera recursiva.
IV. Se agregaron comentarios de eficiencia:
- Se incluyeron comentarios en el código explicando la eficiencia (complejidad) de las operaciones principales.
V. Se actualizaron las clases Usuario y ServidorCorreo:
- Usuario ahora puede tener varias carpetas principales y subcarpetas.
- Se agregaron métodos para mover mensajes y buscar recursivamente desde Usuario y ServidorCorreo.

Los cambios implementados permiten que se puedan gestionar carpetas y subcarpetas como un árbol, mover mensajes entre ellas y realizar busquedas recursivas.

## 02-11
### Informe
Se realizaron cambios para cumplir con la consigna de la tercera entrega y las sugerencias de la devolución anterior:

I. Mejoras en la recursividad según lo sugerido por el profesor:
- Se mejoró el método listar_mensajes para que pueda mostrar mensajes de todas las subcarpetas de manera recursiva
- Se reforzó la recursividad en los métodos de búsqueda y movimiento de mensajes
- Se agregaron pruebas que demuestran la búsqueda en profundidad (carpeta → subcarpeta → sub-subcarpeta)

II. Implementación de filtros automáticos:
- Se agregó un sistema de filtros usando diccionarios para organizar mensajes automáticamente
- Los filtros pueden aplicarse por asunto, remitente o contenido del mensaje
- Cada filtro especifica una carpeta destino donde mover los mensajes que coincidan
- Se pueden crear y eliminar filtros de manera dinámica

III. Implementación de cola de prioridades para mensajes urgentes:
- Se agregó un campo de prioridad a los mensajes
- Se creó una lista ordenada especial para mensajes urgentes
- Los mensajes urgentes se mantienen ordenados alfabéticamente
- Se puede listar mensajes normales, urgentes o ambos

IV. Documentación y pruebas:
- Se agregó documentación detallada sobre la complejidad algorítmica de las operaciones
- Se documentaron los casos borde y su manejo (carpetas vacías, mensajes inexistentes, etc.)
- Se agregaron pruebas exhaustivas para las nuevas funcionalidades
- Se incluyeron ejemplos de uso en el archivo main.py

V. Mejoras en la estructura:
- Se agregaron nuevos métodos manteniendo la modularidad del código
Los cambios implementados mejoran significativamente la funcionalidad del sistema, permitiendo una organización más eficiente de los mensajes a través de filtros automáticos y prioridades, mientras se mantiene la estructura jerárquica de carpetas y la recursividad en las operaciones.
