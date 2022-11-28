from flask import Blueprint, request, redirect, url_for, render_template, flash
from python.MODELS.ModelsCliente import Clientes
from utils.db import db

registros = Blueprint("registros", __name__)


@registros.route("/registro/")
def registro():
    return render_template("registro.html")



@registros.route("/registro_db/", methods=["POST"])
def registro_db():
    message = ""
    if request.method == "POST":
        nombre = request.form["Nombre"]
        apellido = request.form["Apellido"]
        cedula = request.form["Cedula"]
        nacimiento = request.form["nacimiento"]
        telefono = request.form["telefono"]
        email = request.form["Correo"]
        contraseña = request.form["contraseña"]
        try:
            busqueda = (db.session.query(Clientes).filter_by(correo=email).first())
            print(busqueda.id)
            message="ya se encuentra registrado el correo"
        except Exception:
            usuario = Clientes( nombre, apellido, cedula, nacimiento, telefono, email, contraseña )
            db.session.add(usuario)
            db.session.commit()
            try:
                busqueda = (db.session.query(Clientes).filter_by(correo=email).first())
                message = "Registro con exito"
            except Exception:
                message = "Error de Registro"

        flash(message)
        return redirect("/registro/")
          
