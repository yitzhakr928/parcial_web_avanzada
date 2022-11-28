from flask import Blueprint, render_template, request, jsonify
from utils.token.function_jwt import write_token, valida_token
from utils.db import db

logins = Blueprint("login", __name__)


@logins.route("/login/", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@logins.route("/login_auth_token/", methods=["POST"])
def validar_usuario():
    if request.method == "POST":
        name= request.form['usuario']
        password= request.form['password']
        return f"{name}, {password}"
    data = request.get_json()
    if data["username"] == "yitzhak":
        return write_token(data=request.get_json())
        # return f"{type(data)}"
    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response
    

@logins.route("/verify/token")
def verify():
    token=request.headers["Authorization"].split(" ")[1]
    return valida_token(token, output=True)




def consultar_user(user,password):
    user=db.query.filter_by()
    