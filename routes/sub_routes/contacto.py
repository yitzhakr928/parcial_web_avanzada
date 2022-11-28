from flask import Blueprint,render_template

contactos= Blueprint("contacto",__name__)

@contactos.route('/contacto/')
def contacto():
    return render_template('Contacto.html')