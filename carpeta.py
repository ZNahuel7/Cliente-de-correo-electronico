# Clase que representa una carpeta de mensajes (como bandeja de entrada o enviados).
class Carpeta:
    
    def __init__(self, nombre, padre=None):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = [] # Lista de subcarpetas
        self._padre = padre # Referencia a carpeta padre

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def agregar_subcarpeta(self, subcarpeta):
        subcarpeta._padre = self
        self._subcarpetas.append(subcarpeta)

    def get_subcarpetas(self):
        return self._subcarpetas

    def listar_mensajes(self):
        return self._mensajes

    def buscar_mensajes(self, texto, campo="asunto"):
        #Busca mensajes recursivamente por asunto o remitente.
        resultados = []
        for mensaje in self._mensajes:
            if campo == "asunto" and texto.lower() in mensaje.get_asunto().lower():
                resultados.append(mensaje)
            elif campo == "remitente" and texto.lower() in mensaje.get_emisor().get_nombre().lower():
                resultados.append(mensaje)
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensajes(texto, campo))
        return resultados

    def mover_mensaje(self, mensaje, carpeta_destino):
        # Mueve un mensaje de esta carpeta a otra.
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)
            return True
        # Se busca recursivamente en subcarpetas
        for sub in self._subcarpetas:
            if sub.mover_mensaje(mensaje, carpeta_destino):
                return True
        return False

    def get_nombre(self):
        return self._nombre

    def get_padre(self):
        return self._padre
