# Clase que representa una carpeta de mensajes (como bandeja de entrada o enviados).
class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def listar_mensajes(self):
        return self._mensajes

    def get_nombre(self):
        return self._nombre
