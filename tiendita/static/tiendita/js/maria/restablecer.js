$(document).ready(function () {
    $("#restablecer").submit(function (e) {

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
            e.preventDefault();
        }
        else {
            $("#emailalert").html("");
            


        }
        msjMostrar = "";



    });
});