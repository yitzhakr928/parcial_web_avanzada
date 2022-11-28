from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from routes.sub_routes import registro, login, index,contacto
from utils.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/web_avanzada'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(index.indexx)
app.register_blueprint(contacto.contactos)
app.register_blueprint(registro.registros)
app.register_blueprint(login.logins)


db.init_app(app)
with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
