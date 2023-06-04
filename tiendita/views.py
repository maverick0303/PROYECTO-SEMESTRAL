from django.shortcuts import render, redirect
from .models import *
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

#ADMIN
def a_prod_nuevo(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    usuario = Usuario.objects.get(correo = request.user.username)
    if usuario.rol.id_rol == 1:
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
        id_producto = request.POST.get('id_producto')
        producto = Producto.objects.get(cod_producto = id_producto)

        producto.delete()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


    return redirect('producto')

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



#INICIO

def bienvenida(request):
    return render(request, 'tiendita/inicio_sesion/bienvenida.html')

def cerrar_sesion(request):
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

    if Usuario.objects.filter(correo=correoU).exists():
        # El correo ya está registrado, mostrar mensaje de error
        messages.error(request, 'El correo ya está registrado')
        return redirect('nuevo_user')

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

def restablecer(request):
    return render(request,'tiendita/inicio_sesion/restablecer.html')

def verificar(request):
    return render(request,'tiendita/inicio_sesion/verificar.html')

def verificar_agregar(request):
    respuestaR = request.POST['respuesta']

    Pregunta.objects.create(respuesta = respuestaR)
    return redirect('tienda')

#USUARIO

def actu_datos(request):
    usuario = Usuario.objects.get(correo = request.user.username)
    
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    contexto = {
        "datos": usuario,
        "region": region,
        "comuna": comuna
    }
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    return render(request, 'tiendita/usuario/actu_datos.html', contexto)


def carrito(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    return render(request, 'tiendita/usuario/carrito.html')

def histo_compra(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')
    
    return render (request, 'tiendita/usuario/histo_compra.html')

def mod_contra(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Inicie sesión para continuar')
        return redirect('inicio_sesion')

    return render (request, 'tiendita/usuario/mod_contra.html')


