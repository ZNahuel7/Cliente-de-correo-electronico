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
