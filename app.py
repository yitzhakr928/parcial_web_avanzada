from flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/web_avanzada'
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro/')
def registro():
    return render_template('registro.html')


@app.route('/contacto/')
def contacto():
    return render_template('Contacto.html')

@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)