from mensaje import Mensaje
# Clase que representa el servidor de correo, que envia y gestiona mensajes.
class ServidorCorreo:

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
