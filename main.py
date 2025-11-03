from usuario import Usuario
from servidor import ServidorCorreo
from carpeta import Carpeta

# Crear usuarios
nahuel = Usuario("Nahuel", "nahuel@example.com")
lucia = Usuario("Lucía", "lucia@example.com")
marcos = Usuario("Marcos", "marcos@example.com")

# Crear servidor
servidor = ServidorCorreo()

# Crear una carpeta para spam
spam = Carpeta("Spam")
lucia.agregar_carpeta(spam)

# Agregar un filtro automático
lucia.get_buzon().agregar_filtro("filtro_spam", "asunto", "oferta", spam)

# Enviar mensajes entre usuarios
servidor.enviar_mensaje(nahuel, lucia, "Consulta sobre entrega", "Hola Lucía, ¿podrías revisar mi código?")
servidor.enviar_mensaje(lucia, nahuel, "Re: Consulta", "Obvio, ahora lo reviso.")
servidor.enviar_mensaje(marcos, lucia, "Reunión", "Lucía, ¿vas a asistir a la reunión de mañana?")
servidor.enviar_mensaje(nahuel, marcos, "Material de estudio", "Marcos, te paso el material adjunto.")

# Enviar un mensaje urgente
servidor.enviar_mensaje(marcos, lucia, "URGENTE: Reunión pospuesta", "La reunion es pospuesta para la semana que viene", prioridad=1)

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

# Pruebas para 3er entrega
print("\nPRUEBAS DE LA TERCERA ENTREGA:")

# 1. Ver solo mensajes urgentes
print("\nMensajes urgentes de Lucía:")
for m in lucia.get_buzon().listar_mensajes(solo_urgentes=True):
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")

# 2. Probar múltiples filtros
trabajo = Carpeta("Trabajo")
lucia.agregar_carpeta(trabajo)
lucia.get_buzon().agregar_filtro("filtro_trabajo", "remitente", "marcos", trabajo)

# Enviar mensajes que deberían ser filtrados
servidor.enviar_mensaje(marcos, lucia, "Nueva oferta laboral", "¿Te interesa este trabajo?")
servidor.enviar_mensaje(nahuel, lucia, "Super oferta", "¡Mira esta oferta!")

print("\nMensajes en carpeta Spam (filtrado por 'oferta' en asunto):")
for m in spam.listar_mensajes():
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")

print("\nMensajes en carpeta Trabajo (filtrado por remitente 'marcos'):")
for m in trabajo.listar_mensajes():
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")

# 3. Eliminar un filtro y verificar que ya no se aplica
lucia.get_buzon().eliminar_filtro("filtro_spam")
servidor.enviar_mensaje(nahuel, lucia, "Otra oferta", "Esta no debería ir a spam")

print("\nMensaje con 'oferta' después de eliminar filtro (debería estar en bandeja de entrada):")
for m in lucia.get_buzon().listar_mensajes():
    if "oferta" in m.get_asunto().lower():
        print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")

# 4. Probar filtro por contenido del cuerpo
proyectos = Carpeta("Proyectos")
lucia.agregar_carpeta(proyectos)
lucia.get_buzon().agregar_filtro("filtro_proyecto", "cuerpo", "proyecto", proyectos)

servidor.enviar_mensaje(nahuel, lucia, "Update", "Te envío avances del proyecto")
print("\nMensajes en carpeta Proyectos (filtrado por 'proyecto' en cuerpo):")
for m in proyectos.listar_mensajes():
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()} | Cuerpo: {m.get_cuerpo()}")

# 5. Probar orden de mensajes urgentes
servidor.enviar_mensaje(marcos, lucia, "URGENTE: Entrega pendiente", "Revisa esto por favor", prioridad=1)
servidor.enviar_mensaje(nahuel, lucia, "URGENTE: Reunión inmediata", "Conectate a la reunión", prioridad=1)

print("\nMensajes urgentes (deberían estar ordenados alfabéticamente por asunto):")
for m in lucia.get_buzon().listar_mensajes(solo_urgentes=True):
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")

# 6. Probar listado recursivo de mensajes
importantes = Carpeta("Importantes")
lucia.agregar_carpeta(importantes)

# Crear una estructura más profunda de carpetas
subcarpeta_importante = Carpeta("Muy Importantes")
importantes.agregar_subcarpeta(subcarpeta_importante)

# Mover algunos mensajes a las subcarpetas
mensajes_urgentes = lucia.get_buzon().listar_mensajes(solo_urgentes=True)
if mensajes_urgentes:
    mensaje_urgente = mensajes_urgentes[0]
    lucia.mover_mensaje(mensaje_urgente, lucia.get_buzon(), subcarpeta_importante)

print("\nTodos los mensajes de Importantes y sus subcarpetas:")
for m in importantes.listar_mensajes(incluir_subcarpetas=True):
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")

print("\nSolo mensajes urgentes de Importantes y sus subcarpetas:")
for m in importantes.listar_mensajes(solo_urgentes=True, incluir_subcarpetas=True):
    print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")

# Buscar un mensaje urgente y moverlo
mensajes_urgentes = lucia.get_buzon().listar_mensajes(solo_urgentes=True)
if mensajes_urgentes:
    mensaje_urgente = mensajes_urgentes[0]
    lucia.mover_mensaje(mensaje_urgente, lucia.get_buzon(), importantes)
    print("\nMensajes urgentes en carpeta Importantes:")
    for m in importantes.listar_mensajes(solo_urgentes=True):
        print(f"De: {m.get_emisor().get_nombre()} | Asunto: {m.get_asunto()}")
