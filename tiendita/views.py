import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
import requests
from .models import *
from django.http import JsonResponse
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import JsonResponse
from .Carrito import Carrito
from datetime import datetime, timedelta
from django.conf import settings

# Create your views here.

from django.shortcuts import render 
from django.http import HttpResponse 
import requests 


#funcion definitiva
def get_paypal_access_token():
    url = f"{settings.PAYPAL_API_BASE_URL}/v1/oauth2/token"
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US",
    }
    auth = (settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET)
    data = {
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, headers=headers, data=data, auth=auth)
    response.raise_for_status()
    return response.json()['access_token']

def create_order(request):
    if request.method == 'POST':
        usuario = request.user
        carrito = Carrito(request)

        if not carrito.carrito:
            return JsonResponse({"error": "El carrito está vacío."})

        purchase_units = []
        total = 0

        for key, value in carrito.carrito.items():
            total += value['acumulado']
            purchase_units.append({
                "name": value['nombre'],
                "unit_amount": {
                    "currency_code": "USD",
                    "value": str(value['acumulado'] / value['cantidad'])
                },
                "quantity": str(value['cantidad'])
            })

        access_token = get_paypal_access_token()
        url = f"{settings.PAYPAL_API_BASE_URL}/v2/checkout/orders"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        data = {
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    
                    "currency_code": "USD",
                    "value": str(total),
                    "breakdown": {
                        "item_total": {
                            "currency_code": "USD",
                            "value": str(total)
                        }
                    }
                },
                "items": purchase_units
            }],
            "application_context": {
                "return_url": "http://localhost:8000/pago",
                "cancel_url": "http://127.0.0.1:8000/carrito/"
            }
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        order = response.json()
        approval_url = next(link['href'] for link in order['links'] if link['rel'] == 'approve')

        return JsonResponse({"approval_url": approval_url})

    return JsonResponse({"error": "Método de solicitud no válido."})

def execute_payment(request):
    order_id = request.GET.get('token')  # 'token' es el parámetro devuelto por PayPal en la URL

    access_token = get_paypal_access_token()
    url = f"{settings.PAYPAL_API_BASE_URL}/v2/checkout/orders/{order_id}/capture"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post(url, headers=headers)
    response.raise_for_status()
    capture = response.json()
    
    if capture['status'] == 'COMPLETED':
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})




def process_payment(request): 
    if request.method == 'POST': 
        # Datos de la pasarela de pago (en un escenario real, estos serían proporcionados por la pasarela de pago) 
        fakepay_api_key = 'your_fakepay_api_key' 
        fakepay_amount = 100 # Monto a cobrar en centavos ($1.00) 
        
        # Datos del formulario 
        card_number = request.POST['card_number'] 
        expiry_date = request.POST['expiry_date'] 
        cvv = request.POST['cvv']

        # Procesamiento del pago utilizando la pasarela de pago FakePay (ejemplo) 
        response = fakepay_process_payment(fakepay_api_key, fakepay_amount, card_number, expiry_date, cvv) 
        
        # Verificación de la respuesta de la pasarela de pago 
        if response['success']: 
            # El pago fue exitoso 
            return redirect('pago') 
        else: 
            # El pago falló 
            return HttpResponse("Lo siento, ha ocurrido un error durante el procesamiento del pago:  " + response['error']) 
    
    return render(request, 'payment_form.html') 

# Función para procesar el pago utilizando la pasarela de pago FakePay (ejemplo) 
def fakepay_process_payment(api_key, amount, card_number, expiry_date, cvv):  
    # Aquí iría la lógica de conexión y envío de datos a la pasarela de pago real  
    # En este ejemplo, simplemente simularemos un pago exitoso 
    return {'success': True, 'error': ''}

#ADMIN
def a_prod_modificar(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    usuario = Usuario.objects.get(correo = request.user.username)
    if usuario.rol.id_rol == 1:
        # El usuario tiene un rol de usuario (id_rol = 1)
        return redirect('tienda')

    producto = Producto.objects.get(cod_producto = id)
    categoria = Categoria.objects.all()
    contexto = {
        "producto" :producto,
        "categoria" :categoria
    }

    return render(request,'tiendita/admin/prod_modificar.html',contexto)

def a_prod_editar(request):
    idP = request.POST['id']
    nombreP = request.POST['nombre']
    precioP = request.POST['precio']
    categoriaP = request.POST['categoria']
    descripcionP = request.POST['descripcion']
    stockP = request.POST['stock']
    
    producto = Producto.objects.get(cod_producto = idP)

    try:
        fotoP = request.FILES['foto']
    except:
        fotoP = producto.foto

    producto.nombre = nombreP
    producto.precio = precioP
    producto.descripcion = descripcionP
    producto.stock = stockP
    producto.foto = fotoP

    keycategoria = Categoria.objects.get(id_categoria = categoriaP)

    producto.categoria = keycategoria

    producto.save()
    return redirect('tienda')

def a_prod_nuevo(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    usuarioac = Usuario.objects.get(correo = request.user.username)
    if usuarioac.rol.id_rol == 1:
        # El usuario tiene un rol de usuario (id_rol = 1)
        return redirect('tienda')
    
    categoria = Categoria.objects.all()
    contexto = {
        "categoria": categoria
    }
    return render(request,'tiendita/admin/prod_nuevo.html',contexto)

def a_prod_agregar(request):
    nombreP = request.POST['nombre']
    precioP = request.POST['precio']
    categoriaP = request.POST['categoria']
    descripcionP = request.POST['descripcion']
    stockP = request.POST['stock']
    fotoP = request.FILES['foto']

    keycategoria = Categoria.objects.get(id_categoria = categoriaP)

    Producto.objects.create(nombre = nombreP, precio = precioP, descripcion = descripcionP, stock = stockP, foto = fotoP, categoria = keycategoria)

    return redirect('a_prod_nuevo')


def a_prod_eliminar(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Inicie sesión para continuar')
            return redirect('inicio_sesion')
    
        usuarioac = Usuario.objects.get(correo = request.user.username)
        if usuarioac.rol.id_rol == 1:
        # El usuario tiene un rol de usuario (id_rol = 1)
            return redirect('tienda')
        id_producto = request.POST.get('id_producto')
        producto = Producto.objects.get(cod_producto = id_producto)

        producto.delete()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    
def usuarios(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    usuarioac = Usuario.objects.get(correo = request.user.username)
    if usuarioac.rol.id_rol == 1:
        # El usuario tiene un rol de usuario (id_rol = 1)
        return redirect('tienda')

    usuario = Usuario.objects.exclude(correo = request.user.username)

    contexto = {
        "usuario":usuario
    }
    return render (request, 'tiendita/admin/usuarios.html',contexto)

def usuario_rol(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    usuarioac = Usuario.objects.get(correo = request.user.username)
    if usuarioac.rol.id_rol == 1:
        # El usuario tiene un rol de usuario (id_rol = 1)
        return redirect('tienda')
    
    usuario = Usuario.objects.get(correo = id)
    user = User.objects.get(username = id)
    rolus = Rol.objects.get(id_rol = 1)
    rolad  = Rol.objects.get(id_rol = 2)

    if usuario.rol.id_rol == 1:
        usuario.rol = rolad
        user.is_staff = True

        usuario.save()
        user.save()
        return redirect('usuarios')
    else:
        usuario.rol = rolus
        user.is_staff = False

        usuario.save()
        user.save()
        return redirect('usuarios')

def usuario_eliminar(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Inicie sesión para continuar')
            return redirect('inicio_sesion')
    
        usuarioac = Usuario.objects.get(correo = request.user.username)
        if usuarioac.rol.id_rol == 1:
        # El usuario tiene un rol de usuario (id_rol = 1)
            return redirect('tienda')
        
        id_usuario = request.POST.get('id_usuario')
        usuario = Usuario.objects.get(correo = id_usuario)
        direccion = Direccion.objects.get(usuario = usuario)
        user = User.objects.get(username = id_usuario)

        usuario.delete()
        direccion.delete()
        user.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})




#TIENDA
def prod_cuerda(request):
    productos = Producto.objects.filter(categoria = 2)
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(correo = request.user.username)
    else:
        usuario = Usuario.rol.id_rol = 1

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos" :productos,
        "usuario" :usuario
    }
    return render(request,'tiendita/tienda/prod_cuerda.html',contexto)

def prod_idiofono(request):
    productos = Producto.objects.filter(categoria = 3)
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(correo = request.user.username)
    else:
        usuario = Usuario.rol.id_rol = 1

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos" :productos,
        "usuario" :usuario
    }
    return render(request,'tiendita/tienda/prod_idiofono.html',contexto)

def prod_percusion(request):
    productos = Producto.objects.filter(categoria = 1)
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(correo = request.user.username)
    else:
        usuario = Usuario.rol.id_rol = 1

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos" :productos,
        "usuario" :usuario
    }
    return render(request,'tiendita/tienda/prod_percusion.html',contexto)

def prod_viento(request):
    productos = Producto.objects.filter(categoria = 4)
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(correo = request.user.username)
    else:
        usuario = Usuario.rol.id_rol = 1

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos" :productos,
        "usuario" :usuario
    }
    return render(request,'tiendita/tienda/prod_viento.html',contexto)

def tienda(request):
    productos = Producto.objects.all()
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(correo = request.user.username)
    else:
        usuario = Usuario.rol.id_rol = 1

    for producto in productos:
        producto.precio = intcomma(producto.precio)

        contexto = {
        "productos" :productos,
        "usuario" :usuario
        }
    return render(request,'tiendita/tienda/tienda.html',contexto)

def feriados(request):
    return render(request,'tiendita/tienda/feriados.html')


#PRODUCTO

def producto(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    producto = Producto.objects.get(cod_producto = id)
    usuario = Usuario.objects.get(correo = request.user.username)

    producto.precio = intcomma(producto.precio)

    contexto = {
        "producto" :producto,
        "usuario" :usuario
    }
    return render(request,'tiendita/articulos/producto.html',contexto)


def busqueda(request):
    if request.method == "POST":
        buscar = request.POST['buscar']

        resultado = Producto.objects.filter(nombre__contains = buscar)

        return render(request,'tiendita/articulos/busqueda.html', {'buscar':buscar, 'resultado':resultado})
    else:
        return render(request,'tiendita/articulos/busqueda.html')


#INICIO

def bienvenida(request):
    return render(request, 'tiendita/inicio_sesion/bienvenida.html')

def cerrar_sesion(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')

    logout(request)
    messages.info(request, 'Sesion cerrada correctamente')
    return redirect('inicio_sesion')


def inicio_sesion(request):
    return render(request, 'tiendita/inicio_sesion/inicio_sesion.html')

def inicio_sesion_verificar(request):
    nombre1 = request.POST['correo']
    clave1 = request.POST['contraseña']

    try:
        usua1 = User.objects.get(username = nombre1)
    except User.DoesNotExist:
        messages.error(request, 'El usuario o la contraseña son incorrectas')
        return redirect('inicio_sesion')
    
    pass_valida = check_password(clave1, usua1.password)
    if not pass_valida:
        messages.error(request, 'El usuario o la contraseña son incorrectas')
        return redirect('inicio_sesion')
    
    usua = authenticate(username = nombre1, password = clave1)
    if usua is not None:
        login(request, usua)
        return redirect('tienda')
    else:
        messages.error(request, 'El usuario o la contraseña son incorrectas')
        return redirect('inicio_sesion')


def nuevo_user(request):
    pregunta = Pregunta.objects.all()
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    contexto = {
        "region": region,
        "comuna": comuna,
        "pregunta": pregunta
    }

    return render(request, 'tiendita/inicio_sesion/nuevo_user.html',contexto)

def nuevo_user_agregar(request):
    nombreU = request.POST ['nombre']
    rutU = request.POST ['Rut']
    telefonoU = request.POST ['telefono']
    correoU = request.POST ['email']
    contraseñaU = request.POST ['Contraseña']
    comunaU = request.POST ['comuna']
    direccionU = request.POST ['direccion']
    preguntaU = request.POST['pregunta']
    respuestaU = request.POST['respuesta']

    keycomuna = Comuna.objects.get(id_comuna = comunaU)
    keyrol = Rol.objects.get(id_rol = 1)
    keypregunta = Pregunta.objects.get(id_pregunta = preguntaU)

    usuario = Usuario.objects.create(nombre = nombreU, rut = rutU , telefono = telefonoU , correo = correoU , clave = contraseñaU, respuesta = respuestaU , rol = keyrol, pregunta = keypregunta)
    Direccion.objects.create(direccion = direccionU, comuna = keycomuna, usuario = usuario)

    usua = User.objects.create_user(username = correoU, email = correoU, password = contraseñaU)
    usua.is_staff = False
    usua.is_active = True
    usua.save()
    
    return redirect('inicio_sesion')

def verificar_correo(request):
    correo = request.GET.get('correo', None)  # Obtener el valor del correo desde la solicitud GET
    
    # Verificar si el correo existe en la base de datos
    existe_correo = Usuario.objects.filter(correo=correo).exists()
    
    # Devolver una respuesta en formato JSON
    data = {'existe_correo': existe_correo}
    return JsonResponse(data)

def restablecer(request):
    return render(request,'tiendita/inicio_sesion/restablecer.html')

def restablecer_verificar(request):
    correoU = request.POST['correo']
    try:
        usua1 = User.objects.get(username = correoU)
    except User.DoesNotExist:
        messages.error(request, 'El correo ingresado es incorrecto')
        return redirect('restablecer')
    
    if not Usuario.objects.filter(correo=correoU).exists():
        # El correo ya está registrado, mostrar mensaje de error
        messages.error(request, 'El correo ingresado es incorrecto')
        return redirect('restablecer')
    else:
        usua = Usuario.objects.get(correo = correoU)
        return redirect('verificar', id=usua.correo)
    


def verificar(request, id):
    pregunta = Pregunta.objects.all()
    contexto = {
        "pregunta":pregunta,
        "id":id
    }

    return render(request,'tiendita/inicio_sesion/verificar.html',contexto)

def verificar_agregar(request):
    preguntaR = request.POST['pregunta']
    respuestaR = request.POST['respuesta']
    usuarioid = request.POST['usuario']

    usuario = Usuario.objects.get(correo = usuarioid)

    if int(usuario.pregunta.id_pregunta) == int(preguntaR):
        if usuario.respuesta == respuestaR:
            return render(request, 'tiendita/inicio_sesion/recu_contra.html', {'id':usuarioid})
        else:
            messages.error(request, 'La respuesta ingresada es incorrecta')
            return redirect('verificar', id=usuario.correo)
    else:
        messages.error(request, 'La respuesta ingresada es incorrecta')
        return redirect('verificar', id=usuario.correo)

def recu_contra(request):
    usuarioid = request.POST['usuario']
    contra_nueva = request.POST['contra_nueva']

    usuario = Usuario.objects.get(correo = usuarioid)

    user = User.objects.get(username = usuarioid)

    usuario.clave = contra_nueva
    user.set_password(contra_nueva)

    usuario.save()
    user.save()

    return redirect('inicio_sesion')
#USUARIO

def actu_datos(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    usuario = Usuario.objects.get(correo = request.user.username)
    direccion = Direccion.objects.get(usuario = usuario.id_usuario)
    comuna = Comuna.objects.get(id_comuna = direccion.comuna.id_comuna)
    region = Region.objects.get(id_region = comuna.region.id_region)

    contexto = {
        "dire": direccion,
        "datos": usuario,
        "comuna": comuna,
        "region": region

    }
    
    
    return render(request, 'tiendita/usuario/actu_datos.html', contexto)

def actu_2(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')

    usuario = Usuario.objects.get(correo = request.user.username)
    direccion = Direccion.objects.get(usuario = usuario)
    comuna = Comuna.objects.all()
    region = Region.objects.all()
   

    contexto = {
        "dire": direccion,
        "datos": usuario,
        "comuna": comuna,
        "region": region

    }

    return render(request, 'tiendita/usuario/actu_2.html' ,contexto)

def modificarDatos(request):
    nombreU = request.POST['nombre']
    rutU = request.POST['rut']
    telefonoU = request.POST['telefono']
    direccionU = request.POST['direccion']
    comunaU = request.POST['comuna']

    usuario = Usuario.objects.get(correo = request.user.username)
    direccion = Direccion.objects.get(usuario = usuario.id_usuario)
    comuna = Comuna.objects.get(id_comuna = comunaU)

    usuario.nombre = nombreU
    usuario.rut = rutU
    usuario.telefono = telefonoU
    direccion.direccion = direccionU
    direccion.comuna = comuna

    usuario.save()
    direccion.save()    

    return redirect('actu_datos')

def carrito(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    return render(request, 'tiendita/usuario/carrito.html')

def carrito2(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
        
    productos = Producto.objects.all()
   
    for producto in productos:
        producto.precio = intcomma(producto.precio)

        contexto = {
        "productos" :productos    
        }
    return render(request,'tiendita/usuario/carrito.html',contexto)

def add_product(request,id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_producto = id)
    carrito.add(producto)
    contexto = {
        "producto" :producto
    }
    return render(request,'tiendita/usuario/carrito.html', contexto)

def subtract_product(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_producto = id)
    carrito.subtract(producto)
    return redirect ('carrito')

def delete_product(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_producto = id)
    carrito.delete(producto)
    return redirect ('carrito')

def clean_product(request):
    carrito = Carrito(request)
    carrito.clean()
    return redirect ('carrito')

from django.shortcuts import render

def comprar(request):
    from django.db.models import Sum

    f_ventaU = datetime.now()
    f_despachoU = f_ventaU + timedelta(days=1)
    f_entregaU = f_despachoU + timedelta(days=2)
    
    if "carrito" in request.session:
        usuarioU = Usuario.objects.get(correo=request.user)
        reg = Venta.objects.create(f_venta=f_ventaU, f_despacho=f_despachoU, f_entrega=f_entregaU, usuario=usuarioU, carrito=0, total=0)
        Ttotal = 0

        for key, value in request.session["carrito"].items():
            id_prod = value["product_id"]
            cant_prod = int(value["cantidad"])
            producto_comp = Producto.objects.get(cod_producto=id_prod)
            subtotal2 = int(cant_prod) * int(producto_comp.precio)
            Boleta.objects.create(cantidad=cant_prod, subtotal=subtotal2, venta=reg, producto=producto_comp)
            Ttotal += subtotal2

        reg.total = Ttotal
        reg.save()

        total_carrito = Ttotal  # Definir total_carrito como el total calculado
    
        request.session["carrito"] = {}

        return render(request, 'tiendita/usuario/payment_form.html', {'total_carrito': total_carrito})
    else:
        # Si no hay productos en el carrito, puedes manejar este caso de acuerdo a tus necesidades
        return render(request, 'tiendita/usuario/payment_form.html', {'total_carrito': 0, 'total_cantidad': 0})

def pago(request):
    return render (request, 'tiendita/usuario/pago.html')

def histo_compra(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')

    usuarioU = Usuario.objects.get(correo = request.user.username)
    venta = Venta.objects.filter(usuario = usuarioU)
    contexto = {
        'venta':venta
    }
    return render (request, 'tiendita/usuario/histo_compra.html',contexto)

def mod_contra(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')

    return render (request, 'tiendita/usuario/mod_contra.html')

def contra_modificar(request):
    contra_actual = request.POST['contra_actual']
    contra_nueva = request.POST['contra_nueva']

    usuario = Usuario.objects.get(correo = request.user.username)
    user = User.objects.get(username = usuario.correo)

    pass_valida = check_password(usuario.clave, user.password)
    if pass_valida:
        if contra_actual == usuario.clave:
            usuario.clave = contra_nueva
            user.set_password(contra_nueva)

            usuario.save()
            user.save()
        else:
            messages.error(request, 'Contraseña actual incorrecta')
            return redirect('mod_contra')
    else:
        messages.error(request, 'Contraseña actual incorrecta')
        return redirect('mod_contra')

    

    return redirect('actu_datos')

