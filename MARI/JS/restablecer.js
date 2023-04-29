$(document).ready(function () {
    $("#restablecer").submit(function (e) {

        e.preventDefault();


        var correo = $("#correo").val();


        let msjMostrar = "";
        let enviar = false;

        //VALIDACIONES CORREO
        if (correo == "") {
            msjMostrar += "No puede quedar vacio";
            enviar = true;
        }
        else {
            const emailv = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

            if (!emailv.test(correo)) {
                msjMostrar += "Ingrese un correo valido";
                enviar = true;
            }
        }
        if (enviar) {
            $("#emailalert").html(msjMostrar);
        }
        else {
            $("#emailalert").html("");
            window.location.href='http://127.0.0.1:5501/MARI/verificar.html'
        }
        msjMostrar = "";
        enviar = false;


    });
});