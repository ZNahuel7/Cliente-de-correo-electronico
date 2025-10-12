from usuario import Usuario
from servidor import ServidorCorreo

# Crear usuarios
nahuel = Usuario("Nahuel", "nahuel@example.com")
lucia = Usuario("Lucía", "lucia@example.com")
marcos = Usuario("Marcos", "marcos@example.com")

# Crear servidor
servidor = ServidorCorreo()

# Enviar mensajes entre usuarios
servidor.enviar_mensaje(nahuel, lucia, "Consulta sobre entrega", "Hola Lucía, ¿podrías revisar mi código?")
servidor.enviar_mensaje(lucia, nahuel, "Re: Consulta", "Obvio, ahora lo reviso.")
servidor.enviar_mensaje(marcos, lucia, "Reunión", "Lucía, ¿vas a asistir a la reunión de mañana?")
servidor.enviar_mensaje(nahuel, marcos, "Material de estudio", "Marcos, te paso el material adjunto.")

# Listado de mensajes que recibe cada usuario
print("\nMensajes en el buzón de Lucía:")
servidor.listar_mensajes(lucia.get_buzon())

print("\nMensajes en el buzón de Nahuel:")
servidor.listar_mensajes(nahuel.get_buzon())

print("\nMensajes en el buzón de Marcos:")
servidor.listar_mensajes(marcos.get_buzon())

# Prueba de los getters y setters de Mensaje
mensaje_prueba = lucia.get_buzon().listar_mensajes()[0]
print("\nProbando getters y setters de Mensaje:")
print("Asunto original:", mensaje_prueba.get_asunto())
mensaje_prueba.set_asunto("Nuevo Asunto")
print("Asunto modificado:", mensaje_prueba.get_asunto())
print("Cuerpo original:", mensaje_prueba.get_cuerpo())
mensaje_prueba.set_cuerpo("Nuevo cuerpo del mensaje.")
print("Cuerpo modificado:", mensaje_prueba.get_cuerpo())

# Prueba de que Carpeta funciona con varios mensajes
print("\nMensajes en la carpeta de Lucía:")
for m in lucia.get_buzon().listar_mensajes():
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()} | Cuerpo: {m.get_cuerpo()}")

# Probar de un caso de error al enviar un mensaje a un usuario inexistente
def enviar_a_inexistente():
    try:
        servidor.enviar_mensaje(nahuel, None, "Error", "Esto debería fallar.")
    except Exception as e:
        print("\nError al enviar mensaje a usuario inexistente:", e)

enviar_a_inexistente()

