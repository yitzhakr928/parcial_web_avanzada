from persona_asbtrac import persona


class Cliente(persona):

    
    _nombre = ""
    _apellido = ""
    _cedula=""
    _fecha_nacimiento = ""
    _telefono = ""
    _email = ""
    _genero=""
    _pass=""
    _estado = ""

    def __init__(self, nombre,apellido, cedula,fecha_nacimiento, telefono, email,genero,password, estado="ACTIVO"):
        self._nombre = nombre
        self._apellido =apellido
        self._cedula = cedula
        self._fecha_nacimiento= fecha_nacimiento
        self._telefono = telefono
        self._email = email
        self._pass= password
        self._genero= genero
        self._estado = estado


    @property
    def  password(self):
        return self._password

    @password.setter
    def password(self, value):
         self._password=value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value


    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self,value):
        self._fecha_nacimiento = value


    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def  Cedula(self):
        return self._cedula

    @Cedula.setter
    def  Cedula(self, value):
        self._cedula = value

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

    @Email.setter
    def Email(self, email):
        self._email = email





    def agregar(self):
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass
