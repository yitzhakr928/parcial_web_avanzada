class Cancha:

    _tamaño = 0
    _nombre = ""
    _costo = 0
    _disponibilidad = True

    def __init__(self, nombre, costo, disponibilidad):
        self.nombre = nombre
        self.costo = costo
        self.disponibilidad = disponibilidad

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, valor):
        self._tamaño = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, valor):
        self._costo = valor

    @property
    def disponibilidad(self):
        return self._disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, valor):
        self._disponibilidad = valor

    def agregar(self):
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass
