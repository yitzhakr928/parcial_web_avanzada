from flask  import Blueprint, render_template, request, redirect, json
from python.MODELS.ModelsReservas import  Reservas
from utils.db import db

administrador= Blueprint("administrador",__name__ )


@administrador.route("/dashboard/panel/")
def admin():
    return render_template("adminitrador_view.html")


@administrador.route("/dashboard/send-db/")
def send_db():
    nombre_completo= request.args.get("nombre_apellido")
    cedula= request.args.get("Cedula")
    telefono= request.args.get("Telefono")
    email= request.args.get("email")
    cancha=request.args.get("Cancha")
    fecha=request.args.get("fecha")
    duracion=request.args.get("hora")
    
    reserva=Reservas(nombre_completo=nombre_completo, cedula=cedula, telefono=telefono, email=email, cancha=cancha, fecha=fecha, duracion=duracion)
    db.session.add(reserva)
    db.session.commit()
    return redirect("/dashboard/calendar/")
    
  
    
    
@administrador.route("/dashboard/calendar/")
def calendar():
    try:
        data={
            
        }
        canchas={
            "cancha sintetica la patiada Cra. 20 #301, Barranquilla, Atlántico":"cancha1",
            "la cantera centro cormercial carnaval Calle15#16a-96, Soledad, Atlántico":"cancha2",
            "Parque del Sol Cra. 20 #301, Barranquilla, Atlántico":"cancha3",
            "Cancha la Soledeña Cl. 18 #28-69, Soledad, Atlántico":"cancha4"
        }
        reservas= db.session.execute("SELECT * FROM reservas ").fetchall()
        # reservas = Reservas.query.all()
        for reserva in reservas:
            data[f"{reserva[0]}"]={
                "cancha":reserva[5],
                "fecha":reserva[6]
            }
        
        print(data)
    except Exception:
        pass
    return render_template("calendario_view.html", Reservas=data)