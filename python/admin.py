
from persona_asbtrac import Persona

class Admin(Persona):

    _estado=True
    _nombre=""
    _telefono=""
    _email=""

    def __init__(self, estado, nombre, email, telefono):
        self.estado=estado
        self.nombre=nombre
        self.telefono=telefono
        self.email=email
    

    @property
    def Estado(self):
        return self._estado

    @Estado.setter
    def Estado(self, estado):
        self._estado = estado

    @property
    def Nombre(self):
        return self._nombre

    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Telefono(self):
        return self._telefono

    @Telefono.setter
    def Telefono(self, telefono):
        self._telefono = telefono

    @property
    def Email(self):
        return self._email

    @email.setter
    def Email(self, email):
        self._email = email



    def agregar(self):
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass