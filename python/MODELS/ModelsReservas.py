from utils.db import db


class Reservas(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    nombre_completo=db.Column(db.String(200))
    cedula=db.Column(db.Integer())
    telefono=db.Column(db.Integer())
    correo=db.Column(db.String(50))
    cancha= db.Column(db.String(200))
    fecha=db.Column(db.DateTime)
    duracion= db.Column(db.Integer())
    
    def __init__(self,nombre_completo,cedula,email,telefono,cancha,fecha,duracion):
        self.nombre_completo = nombre_completo
        self.cedula =cedula
        self.telefono = telefono
        self.cancha = cancha
        self.fecha = fecha
        self.duracion = duracion
        self.correo=email
 
        
    def __str__(self):
        return {
            "nombre":self.nombre_completo,
            "cedula":self.cedula,
            "telefono":self.telefono,
            "correo":self.correo,
            "cancha":self.cancha,
            "fecha":self.fecha,
            "duracion":self.duracion
        }
    
