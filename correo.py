class Mensaje:
    def __init__(self, emisor, receptor, asunto, cuerpo):
        self._emisor=emisor
        self._receptor=receptor
        self._asunto=asunto
        self._cuerpo=cuerpo
    
    #getters, para acceder a los datos privados del mensaje de manera controlada
    def get_emisor(self):
        return self._emisor
    def get_receptor(self):
        return self._receptor
    def get_asunto(self):
        return self._asunto
    def get_cuerpo(self):
        return self._cuerpo
    
    #setters, para hacer cambios en los datos privados del mensaje de manera controlada
    def set_asunto(self, nuevo_asunto):
        self._asunto = nuevo_asunto
    def set_cuerpo(self, nuevo_cuerpo):
        self._cuerpo = nuevo_cuerpo   

class Usuario:
    def __init__(self, nombre, correo):
        self._nombre=nombre
        self._correo=correo
        self._buzon_entrada=[] #Lista que contiene los mensajes que recibe el usuario
       
    #getters, para acceder a los datos privados del usuario de forma controlada  
    def get_nombre(self):
        return self._nombre
    def get_correo(self):
        return self._correo
    def get_buzon_entrada(self):
        return self._buzon_entrada
    
    #metodo para poder recibir mensajes
    def recibir_correo(self, mensaje):
        self._buzon_entrada.append(mensaje) #se agrega el mensaje al buzón de entrada
        
    #metodo para mostrar los mensajes del buzon de entrada, en forma de lista
    def ver_mensajes(self):
        for m in self._buzon_entrada:
            print(f"De: {m.get_emisor().get_correo()}\n Asunto: {m.get_asunto()}\n Cuerpo: {m.get_cuerpo()}")

class Servidor:
    def __init__(self):
        self._usuarios=[] #Lista de los usuarios que estan registrados en el servidor
    
    def registrar_usuario(self,usuario):
        self._usuarios.append(usuario) #registra al usuario en el servidor
    
    def envio_mensaje(self, mensaje):
        mensaje.get_receptor().recibir_correo(mensaje) #envia el mensaje al usuario receptor

class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre                
        self._mensajes_en_carpeta = []                   

    def get_nombre(self):
        return self._nombre

    def get_bandeja(self):
        return self._mensajes_en_carpeta

    def agregar_mensaje(self, mensaje):
        self._mensajes_en_carpeta.append(mensaje) # Agrega un mensaje a la carpeta

    def eliminar_mensaje(self, mensaje):
        if mensaje in self._mensajes_en_carpeta:
            self._mensajes_en_carpeta.remove(mensaje) # Elimina el mensaje, si existe, de la carpeta

    def listar_mensajes(self):
        for m in self._mensajes_en_carpeta:
            print(f"De: {m.get_emisor().get_correo()}, Asunto: {m.get_asunto()}, Cuerpo: {m.get_cuerpo()}")
    
