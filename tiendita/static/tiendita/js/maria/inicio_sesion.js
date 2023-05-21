$(document).ready(function () {
    $("#inicio").submit(function (e) {

        
        
        var correo = $("#correo").val();

        let msjMostrar = "";
        let enviar = false;

        //VALIDACIONES CORREO
        if (correo == "") {
            msjMostrar += "No puede estar vacio";
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
            $("#correoalert").html(msjMostrar);
            e.preventDefault();
        }
        else {
            $("#correoalert").html("");
            
        }
        msjMostrar = "";
        

        //VALIDAR CONTRASEÑA:

        var contra_actual = $("#clave").val();

        //VALIDACIONES CONTRASEÑA ACTUAL
        if (contra_actual == "") {
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        else {
            if (contra_actual.length < 8) {
                msjMostrar += "Se necesita almenos 8 carácteres";
                enviar = true;
            }

            if (!/[A-ZÑ]/.test(contra_actual)) {
                msjMostrar += "<br>Se necesita almenos 1 carácter mayúscula";
                enviar = true;
            }

            if (!/\d/.test(contra_actual)) {
                msjMostrar += "<br>Se necesita almenos 1 numero";
                enviar = true;
            }

            if (!/[\!\@\#\$\%\^\&\*\(\)\-\+\_\.\,\;\<\>\?\[\]\{\}\=\`\~\|\:]/.test(contra_actual)) {
                msjMostrar += "<br>Se necesita almenos 1 carácter especial";
                enviar = true;
            }
        }
        if (enviar) {
            $("#conactualalert").html(msjMostrar);
            e.preventDefault();
        }
        else {
            $("#conactualalert").html("");
            
            
        }
        msjMostrar = "";
        
        


    });
});