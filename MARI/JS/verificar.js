$(document).ready(function () {
    $("#verificar").submit(function (e) {
        e.preventDefault();
        var respuesta = $("#respuesta").val();

        let msjMostrar = "";
        let enviar = false;

   
        //VALIDAR LAS RESPUESTAS:

        if (respuesta == "") {
            msjMostrar += "No puede quedar vacio ";
            enviar = true;
        }
        else {
            if (respuesta.trim().length < 5) {
                msjMostrar += "La respuesta debe tener almenos 5 caracteres";
                enviar = true;
            }
        }
        if (enviar) {
            
            $("#respalert").html(msjMostrar);
        }
        else {
            $("#respalert").html("");
            window.location.href="http://127.0.0.1:5501/ERNESTO/tienda.html"
        }
        msjMostrar = "";
        enviar = false;
    });
   
});