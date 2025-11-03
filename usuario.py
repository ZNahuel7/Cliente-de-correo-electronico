from carpeta import Carpeta

# Clase que representa a un usuario del sistema de correo.
class Usuario:
    # Análisis de eficiencia:
    # Buscar mensajes en todas las carpetas es O(m) donde m es la cantidad total de mensajes del usuario.
    # Mover mensajes depende de la profundidad del árbol de carpetas.
    def __init__(self, nombre, correo):
        self._nombre = nombre
        self._correo = correo
        self._buzon_entrada = Carpeta("Bandeja de entrada")
        self._carpetas = [self._buzon_entrada]  # Lista de carpetas principales del usuario

    # Getters que permiten acceder a los datos privados del usuario de forma controlada
    def get_nombre(self):
        # Devuelve el nombre del usuario
        return self._nombre

    def get_correo(self):
        # Devuelve el correo del usuario.
        return self._correo

    def get_buzon(self):
        # Devuelve la carpeta de la bandeja de entrada del usuario.
        return self._buzon_entrada

    def get_carpetas(self):
        # Devuelve la lista de carpetas principales del usuario.
        return self._carpetas

    def agregar_carpeta(self, carpeta, padre=None):
        # Agrega una carpeta nueva, como principal o como subcarpeta de otra.
        if padre is None:
            self._carpetas.append(carpeta)
        else:
            padre.agregar_subcarpeta(carpeta)

    def mover_mensaje(self, mensaje, carpeta_origen, carpeta_destino):
        #Mueve un mensaje de una carpeta a otra.
        return carpeta_origen.mover_mensaje(mensaje, carpeta_destino)

    def buscar_mensajes(self, texto, campo="asunto"):
        #Busca mensajes recursivamente en todas las carpetas principales.
        resultados = []
        for carpeta in self._carpetas:
            resultados.extend(carpeta.buscar_mensajes(texto, campo))
        return resultados

    def recibir_mensaje(self, mensaje):
        #Agrega un mensaje a la bandeja de entrada del usuario.
        self._buzon_entrada.agregar_mensaje(mensaje)
        
