# Esta clase representa un mensaje enviado entre usuarios.
class Mensaje:
    def __init__(self, emisor, receptor, asunto, cuerpo):
        self._emisor = emisor
        self._receptor = receptor
        self._asunto = asunto
        self._cuerpo = cuerpo

    # Getters para acceder a los datos privados del mensaje
    def get_emisor(self):
        return self._emisor

    def get_receptor(self):
        return self._receptor

    def get_asunto(self):
        return self._asunto

    def get_cuerpo(self):
        return self._cuerpo

    # Setters para hacer cambios en los datos privados del mensaje
    def set_asunto(self, nuevo_asunto):
        self._asunto = nuevo_asunto

    def set_cuerpo(self, nuevo_cuerpo):
        self._cuerpo = nuevo_cuerpo
