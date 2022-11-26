from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes.registro import registros


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/web_avanzada'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.register_blueprint(registros)
SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacto/')
def contacto():
    return render_template('Contacto.html')


@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template('login.html')

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
