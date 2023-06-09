const form = document.getElementById("form");
$(document).ready(function(){
    $("#form").submit(function(e){

        

        var contra_nueva         = form.connueva.value;
        var contra_verificar     = form.converificar.value;

        let msjMostrar = "";
        let enviar = false;

        //VALIDACIONES CONTRASEÑA NUEVA
        if(contra_nueva==""){
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        else{
            if(contra_nueva.length < 8){
                msjMostrar += "Se necesita almenos 8 carácteres";
                enviar = true;
            }

            if(!/[A-ZÑ]/.test(contra_nueva)){
                msjMostrar += "<br>Se necesita almenos 1 carácter mayúscula";
                enviar = true;
            }

            if(!/\d/.test(contra_nueva)){
                msjMostrar += "<br>Se necesita almenos 1 numero";
                enviar = true;
            }

            if(!/[\!\@\#\$\%\^\&\*\(\)\-\+\_\.\,\;\<\>\?\[\]\{\}\=\`\~\|\:]/.test(contra_nueva)){
                msjMostrar += "<br>Se necesita almenos 1 carácter especial";
                enviar = true;
            }
            
        }
        if(enviar){
            $("#connuevaalert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#connuevaalert").html("");
        }
        msjMostrar = "";
        


        //VALIDACIONES CONTRASEÑA VERIFICAR
        if(contra_verificar==""){
            msjMostrar += "El campo no puede estar vacio";
            enviar = true;
        }
        else{
            if(contra_nueva !== contra_verificar){
                msjMostrar += "Contraseña nueva y Verificar contraseña no son iguales";
                enviar = true;
            }
        }
        if(enviar){
            $("#converificaralert").html(msjMostrar);
            e.preventDefault();
        }
        else{
            $("#converificaralert").html("");
        }
        msjMostrar = "";
        
    });
});