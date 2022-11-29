from flask import Blueprint, render_template, request, jsonify, flash, redirect
from utils.token.function_jwt import write_token, valida_token
from utils.db import db
from  python.MODELS.ModelsCliente import Clientes 

logins = Blueprint("login", __name__)


@logins.route("/login/", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@logins.route("/login_auth_token/", methods=["POST"])
def validar_usuario():
    alerta=""
    if request.method == "POST":
        name= request.form['usuario'].lower()
        password= request.form['password']
        data = consultar_user(name)
        print(data)
        if data["username"] != None and data["password"] != None:
            if data["username"] == name:
                if data["password"] != password:
                    alerta="Datos incorrectos"
                    return redirect("/login/")
                else:
                     print(write_token(data=data))
                     return redirect("/dashboard/panel/")
            else:
                response = jsonify({"message": "User not found"})
                response.status_code = 404
                return response
        else:
            alerta="Usuario No registrado"
            return redirect("/login/")
    flash(alerta)


@logins.route("/verify/token")
def verify():
    token=request.headers["Authorization"].split(" ")[1]
    return valida_token(token, output=True)




def consultar_user(user):
    data={
            "username":None,
            "password":None,
        }
    try:
        user=db.session.query(Clientes).filter_by(nombre=user).first()
        data={
            "username":user.nombre,
            "password":user.contraseña
        } 
    except Exception:
        pass
    
    return data    