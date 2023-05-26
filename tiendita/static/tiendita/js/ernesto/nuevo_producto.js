$(document).ready(function(){
    $("#form").submit(function(e){

        


        var nombre         = $("#prodname").val(); 
        var precio         = $("#prodprice").val();
        var tipo           = $("#prodtype").val();
        var descripcion    = $("#proddesc").val();
        var existencias    = $("#prodstock").val();
        var foto           = $("#prodfoto");

        let msjMostrar = "";
        let enviar = false;


        //VALIDACIONES NOMBRE
        if(nombre==""){
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
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
        

        
        //VALIDACIONES PRECIO
        if(precio==""){
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        else{
            if(!/^[\d]+$/.test(precio)){
                msjMostrar += "El precio no puede tener caracteres especiales o letras";
                enviar = true;
            }
        }
        if(enviar){
            $("#pricealert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#pricealert").html("");
        }
        msjMostrar = "";
        


        //VALIDACIONES DESCRIPCION
        if(descripcion==""){
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        if(enviar){
            $("#descalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#descalert").html("");
        }
        msjMostrar = "";
        
        

        //VALIDACIONES STOCK
        if(existencias==""){
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        else{
            if(!/^[\d]+$/.test(existencias)){
                msjMostrar += "El stock no puede tener caracteres especiales o letras";
                enviar = true;
            }
        }
        if(enviar){
            $("#stockalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#stockalert").html("");
        }
        msjMostrar = "";
        

        
        //VALIDACIONES IMAGEN
        if(foto.val()==""){
            msjMostrar += "Seleccione una imagen";
            enviar = true;
        }
        else{
            //CONSEGUIR ALTO Y ANCHO
            const file = foto[0].files[0];
            const reader = new FileReader();

            reader.onload = function(event) {
                const img = new Image();
                img.onload = function() {
                    const width = this.width;
                    const height = this.height;
                    
                    //VALIDAR ALTO Y ANCHO
                    if(width !== height){
                        msjMostrar += "El alto y ancho de la imagen tienen que ser iguales";
                        enviar = true;
                    }

                    if(enviar){
                        $("#fotoalert").html(msjMostrar);
                        e.preventDefault();
                    }
                    else{
                        $("#fotoalert").html("");
                    }
                    msjMostrar = "";
                    

                }
                img.src = event.target.result;
            }
            reader.readAsDataURL(file);

            
        }

        if(enviar){
            $("#fotoalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#fotoalert").html("");
        }
        msjMostrar = "";
        

    });
});