$(document).ready(function () {
    $("#verificar").submit(function (e) {
        
        var respuesta = $("#respuesta").val();

        let msjMostrar = "";
        let enviar = false;

   
        //VALIDAR LAS RESPUESTAS:

        if (respuesta == "") {
            msjMostrar += "No puede quedar vacio ";
            enviar = true;
        }

        if (enviar) {
            
            $("#respalert").html(msjMostrar);
            e.preventDefault();
        }
        else {
            $("#respalert").html("");
           
        }
        msjMostrar = "";
        
    });
   
});