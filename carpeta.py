# Clase que representa una carpeta de mensajes (como bandeja de entrada o enviados).
class Carpeta:
    
    def __init__(self, nombre, padre=None):
        self._nombre = nombre
        self._mensajes = []  # Lista para mensajes normales
        self._mensajes_urgentes = []  # Lista ordenada para mensajes urgentes
        self._subcarpetas = [] # Lista de subcarpetas
        self._padre = padre # Referencia a carpeta padre
        self._filtros = {}  # Diccionario de filtros automáticos

    def agregar_mensaje(self, mensaje):
        # Primero aplicamos los filtros automáticos
        if self._aplicar_filtros(mensaje):
            return
            
        # Si el mensaje es urgente, lo agregamos a la cola de prioridad
        if mensaje.get_prioridad() == 1:
            self._insertar_urgente(mensaje)
        else:
            self._mensajes.append(mensaje)
            
    def _insertar_urgente(self, mensaje):
        # Inserción ordenada en la lista de mensajes urgentes
        self._mensajes_urgentes.append(mensaje)
        i = len(self._mensajes_urgentes) - 1
        while i > 0 and self._mensajes_urgentes[i-1].get_asunto() > mensaje.get_asunto():
            self._mensajes_urgentes[i] = self._mensajes_urgentes[i-1]
            i -= 1
        self._mensajes_urgentes[i] = mensaje
        
    def agregar_filtro(self, nombre, campo, valor, carpeta_destino):
        # Crea un filtro nuevo para mover mensajes automáticamente
        # El campo puede ser: asunto, remitente o cuerpo del mensaje
        self._filtros[nombre] = {
            'campo': campo,
            'valor': valor.lower(),
            'destino': carpeta_destino
        }
        
    def eliminar_filtro(self, nombre):
        if nombre in self._filtros:
            del self._filtros[nombre]
            
    def _aplicar_filtros(self, mensaje):
        # Revisa si el mensaje coincide con algún filtro y lo mueve
        # Devuelve True si se movió el mensaje
        for filtro in self._filtros.values():
            if filtro['campo'] == 'asunto' and filtro['valor'] in mensaje.get_asunto().lower():
                filtro['destino'].agregar_mensaje(mensaje)
                return True
            elif filtro['campo'] == 'remitente' and filtro['valor'] in mensaje.get_emisor().get_nombre().lower():
                filtro['destino'].agregar_mensaje(mensaje)
                return True
            elif filtro['campo'] == 'cuerpo' and filtro['valor'] in mensaje.get_cuerpo().lower():
                filtro['destino'].agregar_mensaje(mensaje)
                return True
        return False

    def agregar_subcarpeta(self, subcarpeta):
        subcarpeta._padre = self
        self._subcarpetas.append(subcarpeta)

    def get_subcarpetas(self):
        return self._subcarpetas

    def listar_mensajes(self, solo_urgentes=False, incluir_subcarpetas=False):
        # Devuelve los mensajes de la carpeta. 
        # Si solo_urgentes es True, solo muestra los urgentes
        # Si incluir_subcarpetas es True, busca también en las subcarpetas
        if solo_urgentes:
            mensajes = self._mensajes_urgentes[:]
        else:
            mensajes = self._mensajes_urgentes + self._mensajes
            
        # Si se piden mensajes de subcarpetas, los agregamos recursivamente
        if incluir_subcarpetas:
            for subcarpeta in self._subcarpetas:
                mensajes.extend(subcarpeta.listar_mensajes(solo_urgentes, True))
                
        return mensajes

    def buscar_mensajes(self, texto, campo="asunto"):
        # Busca mensajes que contengan el texto en el campo especificado
        # Si la carpeta está vacía devuelve una lista vacía
        # Si el campo no es válido, busca en el asunto
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
        # Mueve un mensaje a otra carpeta
        # Si el mensaje no existe o la carpeta destino es None, devuelve False
        # Si encuentra y mueve el mensaje, devuelve True
        if carpeta_destino is None:
            return False
            
        # Buscar en mensajes normales
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)
            return True
            
        # Buscar en mensajes urgentes
        if mensaje in self._mensajes_urgentes:
            self._mensajes_urgentes.remove(mensaje)
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
