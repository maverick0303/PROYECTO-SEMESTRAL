$(document).ready(function () {

    $("#nuevo").submit(function (e) {
        e.preventDefault();
        
        var nombre = $("#nombre").val();
        var apellido = $("#apellido").val();
        var rut = $("#rut").val();
        var telefono = $("#telefono").val();
        var correo = $("#correo").val();
        var contra_nueva = nuevo.connueva.value;
        var contra_verificar = nuevo.converificar.value;
        var direccion = $("#direccion").val();

        let msjMostrar = "";
        let enviar = false;
        //VALIDAR NOMBRE
        if (nombre == "") {
            msjMostrar += "No puede estar vacio";
            enviar = true;

        }
        else {
            if (nombre.trim().length < 5) {
                msjMostrar += "Debe de tener almenos 5 caracteres";
                enviar = true;
            }
            if (!/^[a-zñA-ZÑ\s]+$/.test(nombre)) {
                msjMostrar += "<br> No puede tener caracteres especiales,ni numeros";
                enviar = true;
            }
        }
        if (enviar) {
            $("#namealert").html(msjMostrar);
        }
        else {
            $("#namealert").html("");


        }
        msjMostrar = "";
        

        //VALIDAR APELLIDO:



        if (apellido == "") {
            msjMostrar += "No puede estar vacio";
            enviar = true;

        }
        else {
            if (apellido.trim().length < 5) {
                msjMostrar += "Debe de tener almenos 5 caracteres";
                enviar = true;
            }
            if (!/^[a-zñA-ZÑ\s]+$/.test(apellido)) {
                msjMostrar += "<br>No puede tener caracteres especiales, ni numeros";
                enviar = true;
            }
        }
        if (enviar) {
            $("#apellialert").html(msjMostrar);
        }
        else {
            $("#apellialert").html("");

        }
        msjMostrar = "";
        

        //VALIDAR RUT:
        if (rut == "") {
            msjMostrar += "No puede ir vacio";
            enviar = true;
        }
        else {
            const rutv = /^[0-9]{1,2}\.[0-9]{3}\.[0-9]{3}-[0-9kK]{1}$/;

            if (!rutv.test(rut)) {
                msjMostrar += "Ingrese un rut valido";
                enviar = true;
            }
        }
        if (enviar) {
            $("#rutalert").html(msjMostrar);
        }
        else {
            $("#rutalert").html("");

        }
        msjMostrar = "";
        

        //VALIDAR TELEFONO:

        if (telefono == "") {
            msjMostrar += "No puede ir vacio"
            enviar = true;
        }
        else {
            const phonov = /^\+[0-9]{11}$/;

            if (!phonov.test(telefono)) {
                msjMostrar += "Ingrese un numero de telefono valido";
                enviar = true;
            }
        }
        if (enviar) {
            $("#phonealert").html(msjMostrar);
        }
        else {
            $("#phonealert").html("");
        }
        msjMostrar = "";
        

        //VALIDAR CORREO:

        if (correo == "") {
            msjMostrar += "No puede ir vacio";
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
        }
        msjMostrar = "";
        

        //VALIDAR CONTRASEÑA Y REPETIR CONTRASEÑA:

        if (contra_nueva == "") {
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        else {
            if (contra_nueva.length < 8) {
                msjMostrar += "Se necesita almenos 8 carácteres";
                enviar = true;
            }

            if (!/[A-ZÑ]/.test(contra_nueva)) {
                msjMostrar += "<br>Se necesita almenos 1 carácter mayúscula";
                enviar = true;
            }

            if (!/\d/.test(contra_nueva)) {
                msjMostrar += "<br>Se necesita almenos 1 numero";
                enviar = true;
            }

            if (!/[\!\@\#\$\%\^\&\*\(\)\-\+\_\.\,\;\<\>\?\[\]\{\}\=\`\~\|\:]/.test(contra_nueva)) {
                msjMostrar += "<br>Se necesita almenos 1 carácter especial";
                enviar = true;
            }
        }
        if (enviar) {
            $("#connuevaalert").html(msjMostrar);
        }
        else {
            $("#connuevaalert").html("");
        }
        msjMostrar = "";
        

        //REPETIR CONTRASEÑA:

        if (contra_verificar == "") {
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        else {
            if (contra_nueva !== contra_verificar) {
                msjMostrar += "Contraseña nueva y Verificar contraseña no son iguales";
                enviar = true;
            }
        }
        if (enviar) {
            $("#converificaralert").html(msjMostrar);
        }
        else {
            $("#converificaralert").html("");
        }
        msjMostrar = "";
        

        //VERIFICAR DIRECCION:

        if (direccion == "") {
            msjMostrar += "No puede estar vacio";
            enviar = true;
        }

        if (enviar) {
            $("#direccionalert").html(msjMostrar);

        }
        else {
            $("#direccionalert").html("");
            window.location.href = "http://127.0.0.1:5501/MARI/inicio_sesion.html";
        }

        
        
        msjMostrar = "";
        
       
        
    });
    
});

