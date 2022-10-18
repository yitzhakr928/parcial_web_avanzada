var agregar=document.getElementById("obj");
var objetos=document.getElementById("Objetos");
var anexar=document.getElementById("boton_agregar")

var agregarobjeto=function(){
   var lista=[];
   var div=document.createElement("div");//crea elemento div
   var selec=document.createElement("select");//crea elemento select
   var cant=document.createElement("input");//crea elemento input
   cant.setAttribute("type","number");//agrega atributos
   cant.setAttribute("class","cantidad");//agrega atributos
   var boton=document.createElement("input");//crear elemento
   boton.setAttribute("type","button");//agrega atributos
   boton.setAttribute("id","eliminar");//agrega atributos
   boton.setAttribute("value","X");//agrega atributos
  
    for (let i = 0; i < objetos.length; i++) {
        lista[i]=objetos[i].innerHTML;  //guardamos los elementos del objetos en un array
    };
   
    for (let i = 0; i < lista.length; i++) {
        var option=document.createElement("option")//creamos el elemento option
        var contenido=document.createTextNode(lista[i]);
        option.appendChild(contenido);
        option.setAttribute("value",i);
        selec.appendChild(option);
    }

    for (var i = 0; i <= agregar.children.length -1; i++) {
        agregar.children[i].addEventListener("click", function(){
            this.parentNode.removeChild(this);
        });
    }

   selec.setAttribute("name","obejetos-aquiler");
   div.appendChild(selec);
   div.appendChild(cant);
   div.appendChild(boton);
   div.setAttribute("class","agg");
   agregar.appendChild(div);

   console.log("sale");
}

anexar.addEventListener('click',agregarobjeto);




var eleminarTarea = function(){
    this.parentNode.removeChild(this);
};

// Borrando Elementos de la lista
for (var i = 0; i <= agregar.children.length -1; i++) {
   agregar.children[i].addEventListener("click", eleminarTarea);
}



//verificacion de datos

