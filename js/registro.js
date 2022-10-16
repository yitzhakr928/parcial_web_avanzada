var verificacion=document.getElementsByClassName("formato");


for (let i = 0; i < verificacion.length; i++) {
    var palabra=verificacion[i].value; 

    //campos vacios
   if(palabra==""){
        if(i==0){
            console.log("llene el campo nombre")
        }else if(i==1){
            console.log("LLene el campo apellido")
        }else if(i==2){
            console.log("LLene el campo cedula")
        }else if(i==3){
            console.log("LLene el campo fecha")
        }else if(i==4){
            console.log("LLene el campo correo")
        }else if(i==5){
            console.log("LLene el campo contrseña")
        }
   }
}

