from utils.db import db


class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    cedula = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    telefono = db.Column(db.String(15))
    correo = db.Column(db.String(50), unique=True)
    contraseña = db.Column(db.String(20))

    def __init__(self, nombre, apellido, cedula, fecha, telefono, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha = fecha
        self.telefono = telefono
        self.correo = correo
        self.contraseña = contraseña

    