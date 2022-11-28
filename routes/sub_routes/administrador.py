from flask  import Blueprint, render_template

administrador= Blueprint("administrador",__name__ )

@administrador.route("/dashboard/panel/")
def admin():
    return render_template("administrador.html")