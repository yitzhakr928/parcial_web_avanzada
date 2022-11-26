from flask import Blueprint, request, redirect, url_for,render_template
from python.cliente import  Cliente

registros= Blueprint('registros',__name__)


@registros.route('/registro/')
def registro():
    return render_template('registro.html')


@registros.route('/registro_db/', methods=["POST"])
def registro_db():
    if request.method == "POST":
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        cedula = request.form['Cedula']
        nacimiento = request.form['nacimiento']
        telefono = request.form['telefono']
        email = request.form['Correo']
        # print(nombre,apellido,cedula,nacimiento,telefono,email)
        usuario = Cliente( nombre=nombre,apellido=apellido,cedula=cedula,fecha_nacimiento=nacimiento,telefono=telefono,email=email)
        
        # print(usuario.__str__())
        return redirect(url_for("registro"))
