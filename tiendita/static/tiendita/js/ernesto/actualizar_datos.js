$(document).ready(function(){
    
    const $region = $('#region');
    const $comuna = $('#comuna');

    $region.change(function () {
        $comuna.val('');

        $comuna.prop('disabled', !Boolean($region.val()));
        $comuna.find('option[data-region]').hide();
        $comuna.find('option[data-region="' + $region.val() + '"]').show();
    });
    $("#form").submit(function(e){

        

        var nombre      = $("#name").val(); 
        var apellido    = $("#apelli").val();
        var correo      = $("#email").val();
        var telefono    = $("#phone").val();
        var comuna      = $("#second-select").val();
        var direccion   = $("#direc").val();
        var rut         = $("#rut").val();

        let msjMostrar = "";
        let enviar = false;


        //VALIDACIONES NOMBRE
        if(nombre==""){
        }
        else{
            
    
            if(!/^[a-zñA-ZÑ\s]+$/.test(nombre)){
                msjMostrar += "<br>El nombre no puede tener caracteres especiales o numeros";
                enviar = true;
            }
        }
        if(enviar){
            $("#namealert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#namealert").html("");
        }
        msjMostrar = "";
        


        //VALIDACIONES APELLIDO
        if(apellido==""){
        }
        else{
           
    
            if(!/^[a-zñA-ZÑ\s]+$/.test(apellido)){
                msjMostrar += "<br>El apellido no puede tener caracteres especiales o numeros";
                enviar = true;
            }
        }
        if(enviar){
            $("#apellialert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#apellialert").html("");
        }
        msjMostrar = "";
        


        //VALIDACIONES CORREO
        if(correo==""){
        }
        else{
            const emailv = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

            if(!emailv.test(correo)){
                msjMostrar += "Ingrese un correo valido";
                enviar = true;
            }
        }
        if(enviar){
            $("#emailalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#emailalert").html("");
        }
        msjMostrar = "";
        


        //VALIDACIONES TELEFONO
        if(telefono==""){
        }
        else{
            const phonov = /^\+[0-9]{11}$/;

            if(!phonov.test(telefono)){
                msjMostrar += "Ingrese un numero de telefono valido";
                enviar = true;
            }
        }
        if(enviar){
            $("#phonealert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#phonealert").html("");
        }
        msjMostrar = "";
        


        //VALIDACIONES COMUNA
        if(comuna=="o1"){
            msjMostrar += "seleccione una comuna";
            enviar = true;
        }
        if(enviar){
            $("#comunaalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#comunaalert").html("");
        }
        msjMostrar = "";



        //VALIDACIONES DIRECCION
        if(direccion==""){
        }
        else{
            if(direccion.trim().length < 5){
                msjMostrar += "La direccion debe tener almenos 5 caracteres";
                enviar = true;
            }

            if(!/^[a-zñA-ZÑ0-9\s\.\#]+$/.test(direccion)){
                msjMostrar += "<br>La direccion no puede tener caracteres especiales excepto '.' '#' ' '";
                enviar = true;
            }
        }
        if(enviar){
            $("#direcalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#direcalert").html("");
        }
        msjMostrar = "";



        //VALIDACIONES RUT
        if(rut==""){
        }
        else{
            const rutv = /^[0-9]{1,2}\.[0-9]{3}\.[0-9]{3}-[0-9kK]{1}$/;

            if(!rutv.test(rut)){
                msjMostrar += "Ingrese un rut con puntos y guio";
                enviar = true;
            }
        }
        if(enviar){
            $("#rutalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#rutalert").html("");
        }
        msjMostrar = "";
        

    });
});