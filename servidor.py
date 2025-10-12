from mensaje import Mensaje
# Clase que representa el servidor de correo, que envia y gestiona mensajes.
class ServidorCorreo:
    def mover_mensaje(self, usuario, mensaje, carpeta_origen, carpeta_destino):
        # Mueve un mensaje de una carpeta a otra para un usuario
        return usuario.mover_mensaje(mensaje, carpeta_origen, carpeta_destino)

    def buscar_mensajes(self, usuario, texto, campo="asunto"):
        # Busca mensajes recursivamente en todas las carpetas del usuario
        return usuario.buscar_mensajes(texto, campo)

    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        #Crea y envía un mensaje del remitente al destinatari
        mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)
        destinatario.recibir_mensaje(mensaje)

    def recibir_mensaje(self, usuario, mensaje):
        #Entrega un mensaje a un usuario
        usuario.recibir_mensaje(mensaje)

    def listar_mensajes(self, carpeta):
        #Lista los mensajes de una carpeta determinada
        for mensaje in carpeta.listar_mensajes():
            print(f"De: {mensaje.get_emisor().get_nombre()} | Asunto: {mensaje.get_asunto()}")
