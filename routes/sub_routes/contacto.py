from flask import Blueprint,render_template

contacto= Blueprint("contacto",__name__)

@contacto.route('/contacto/')
def contacto():
    return render_template('Contacto.html')