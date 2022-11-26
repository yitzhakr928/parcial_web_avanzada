from flask import Blueprint, request, redirect, url_for,render_template
from python.MODELS.ModelsCliente import Clientes
from utils.db import db

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
        contraseña= request.form['contraseña']
        usuario=Clientes(nombre,apellido,cedula,nacimiento,telefono,email,contraseña)
        db.session.add(usuario)
        db.session.Commit()
        return redirect(url_for("registro"))
