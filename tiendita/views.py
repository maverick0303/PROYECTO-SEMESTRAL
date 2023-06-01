from django.shortcuts import render, redirect
from .models import *
from django.contrib.humanize.templatetags.humanize import intcomma
# Create your views here.

#ADMIN
def a_bombo(request):
    return render(request,'tiendita/admin/bombo.html')

def a_prod_cuerda(request):
    return render(request,'tiendita/admin/prod_cuerda.html')

def a_prod_idiofono(request):
    return render(request,'tiendita/admin/prod_idiofono.html')

def a_prod_percusion(request):
    return render(request,'tiendita/admin/prod_percusion.html')

def a_prod_viento(request):
    return render(request,'tiendita/admin/prod_viento.html')

def a_prod_nuevo(request):
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

def a_tienda(request):
    return render(request,'tiendita/admin/tienda.html')


#TIENDA
def prod_cuerda(request):
    productos = Producto.objects.filter(categoria = 2)

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos":productos
    }
    return render(request,'tiendita/tienda/prod_cuerda.html',contexto)

def prod_idiofono(request):
    productos = Producto.objects.filter(categoria = 3)

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos":productos
    }
    return render(request,'tiendita/tienda/prod_idiofono.html',contexto)

def prod_percusion(request):
    productos = Producto.objects.filter(categoria = 1)

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos":productos
    }
    return render(request,'tiendita/tienda/prod_percusion.html',contexto)

def prod_viento(request):
    productos = Producto.objects.filter(categoria = 4)

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos":productos
    }
    return render(request,'tiendita/tienda/prod_viento.html',contexto)

def tienda(request):
    productos = Producto.objects.all()

    for producto in productos:
        producto.precio = intcomma(producto.precio)

    contexto = {
        "productos":productos
    }
    return render(request,'tiendita/tienda/tienda.html',contexto)

def feriados(request):
    return render(request,'tiendita/tienda/feriados.html')


#PRODUCTO
def producto(request, id):
    producto = Producto.objects.get(cod_producto = id)

    producto.precio = intcomma(producto.precio)

    contexto = {
        "producto": producto
    }
    return render(request,'tiendita/articulos/producto.html',contexto)



#INICIO

def bienvenida(request):
    return render(request,'tiendita/inicio_sesion/bienvenida.html')

def inicio_sesion(request):
    return render(request, 'tiendita/inicio_sesion/inicio_sesion.html')

def nuevo_user(request):
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    contexto = {
        "region": region,
        "comuna": comuna
    }

    return render(request, 'tiendita/inicio_sesion/nuevo_user.html',contexto)

def nuevo_user_agregar(request):
    nombre = request.POST ['nombre']
    rut = request.POST ['Rut']
    telefono = request.POST ['telefono']
    correo = request.POST ['email']
    contraseña = request.POST ['Contraseña']

    region = request.POST ['region']
    

    Usuario.objects.create(nombre = nombre, rut = rut , telefono = telefono , correo = correo , contraseña = clave)
    
    return redirect('tienda')

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
    return render(request, 'tiendita/usuario/actu_datos.html')

def carrito(request):
    return render(request, 'tiendita/usuario/carrito.html')

def histo_compra(request):
    return render (request, 'tiendita/usuario/histo_compra.html')

def mod_contra(request):

    return render (request, 'tiendita/usuario/mod_contra.html')


