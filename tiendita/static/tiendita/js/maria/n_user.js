$(document).ready(function () {
      //validar la comuna y la region:

      const $region = $('#region');
      const $comuna = $('#comuna');

      $region.change(function () {
          $comuna.val('');

          $comuna.prop('disabled', !Boolean($region.val()));
          $comuna.find('option[data-region]').hide();
          $comuna.find('option[data-region="' + $region.val() + '"]').show();
      });
    $("#nuevo").submit(function (e) {

        var nombre = $("#nombre").val();
        var apellido = $("#apellido").val();
        var rut = $("#rut").val();
        var telefono = $("#telefono").val();
        var correo = $("#correo").val();
        var correoUtilizado = $("#correoUtilizado").val();
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

            if (!/^[a-zñA-ZÑ\s]+$/.test(nombre)) {
                msjMostrar += "<br> No puede tener caracteres especiales, ni numeros";
                enviar = true;
            }
        }
        if (enviar) {
            $("#namealert").html(msjMostrar);
            e.preventDefault();
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

            if (!/^[a-zñA-ZÑ\s]+$/.test(apellido)) {
                msjMostrar += "<br>No puede tener caracteres especiales, ni numeros";
                enviar = true;
            }
        }
        if (enviar) {
            $("#apellialert").html(msjMostrar);
            e.preventDefault();

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
            e.preventDefault();
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
            e.preventDefault();
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

            if (correoUtilizado == "true") {
                msjMostrar += "correo ya utilizado";
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
            e.preventDefault();
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
            e.preventDefault();
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
        else {
            if (direccion.trim().length < 5) {
                msjMostrar += "La direccion debe tener almenos 5 caracteres";
                enviar = true;
            }

            if (!/^[a-zñA-ZÑ0-9\s\.\#]+$/.test(direccion)) {
                msjMostrar += "<br>La direccion no puede tener caracteres especiales excepto '.' '#' ' '";
                enviar = true;
            }
        }

        if (enviar) {
            $("#direccionalert").html(msjMostrar);
            e.preventDefault();


        }
        else {
            $("#direccionalert").html("");

        }



        msjMostrar = "";
        var respuesta = $("#respuesta").val();

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

