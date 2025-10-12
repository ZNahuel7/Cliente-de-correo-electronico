from carpeta import Carpeta

# Clase que representa a un usuario del sistema de correo.
class Usuario:
    def __init__(self, nombre, correo):
        self._nombre = nombre
        self._correo = correo
        self._buzon_entrada = Carpeta("Bandeja de entrada")

    # Getters que permiten acceder a los datos privados del usuario de forma controlada
    def get_nombre(self):
        #Devuelve el nombre del usuario
        return self._nombre

    def get_correo(self):
        #Devuelve el correo del usuario.
        return self._correo

    def get_buzon(self):
        #Devuelve la carpeta de la bandeja de entrada del usuario.
        return self._buzon_entrada

    def recibir_mensaje(self, mensaje):
        #Agrega un mensaje a la bandeja de entrada del usuario.
        self._buzon_entrada.agregar_mensaje(mensaje)