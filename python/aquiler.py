from persona_asbtrac import Persona


class Alquiler(Persona):

    _numAlquiler = 0
    _nombre = ""
    _fechaAlquiler = ""
    _HoraAlquiler = ""
    _descripcion = ""
    _estado = False
    _pago = ""

    def __init__(
        self,
        numAlquiler,
        nombre,
        fechaAlquiler,
        HoraAlquiler,
        descripcion,
        estado,
        pago,
    ):
        self.numAlquiler = numAlquiler
        self.nombre = nombre
        self.fechaAlquiler = fechaAlquiler
        self.HoraAlquiler = HoraAlquiler
        self.descripcion = descripcion
        self.estado = estado
        self.pago = pago

    @property
    def numAlquiler(self):
        return self._numAlquiler

    @numAlquiler.setter
    def numAlquiler(self, num):
        self._numAlquiler = num

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fechaAlquiler(self):
        return self._fechaAlquiler

    @fechaAlquiler.setter
    def fechaAlquiler(self, fecha):
        self._fechaAlquiler = fecha

    @property
    def HoraAlquiler(self):
        return self._HoraAlquiler

    @HoraAlquiler.setter
    def HoraAlquiler(self, Hora):
        self._HoraAlquiler = Hora

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def pago(self):
        return self._pago

    @pago.setter
    def pago(self, pago):
        self._pago = pago

    def agregar(self):
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass
