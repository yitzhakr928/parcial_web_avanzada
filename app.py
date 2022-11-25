from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from python.cliente import  Cliente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cable_exito'
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registro/')
def registro():
    return render_template('registro.html')


@app.route('/registro_db/', methods=["POST"])
def registro_db():
    if request.method == "POST":
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        cedula = request.form['Cedula']
        nacimiento = request.form['nacimiento']
        telefono = request.form['telefono']
        email = request.form['Correo']
        # print(nombre,apellido,cedula,nacimiento,telefono,email)
        usuario =Cliente( nombre=nombre,apellido=apellido,cedula=cedula,fecha_nacimiento=nacimiento,telefono=telefono,email=email)
        
        # print(usuario.__str__())
        return redirect(url_for("registro"))


@app.route('/contacto/')
def contacto():
    return render_template('Contacto.html')


@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
