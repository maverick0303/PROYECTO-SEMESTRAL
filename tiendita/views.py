from django.shortcuts import render, redirect
from .models import *
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
    return render(request,'tiendita/tienda/prod_cuerda.html')

def prod_idiofono(request):
    return render(request,'tiendita/tienda/prod_idiofono.html')

def prod_percusion(request):
    return render(request,'tiendita/tienda/prod_percusion.html')

def prod_viento(request):
    return render(request,'tiendita/tienda/prod_viento.html')

def feriados(request):
    return render(request,'tiendita/tienda/feriados.html')

def tienda(request):
    productos = Producto.objects.all()
    contexto = {
        "productos":productos
    }
    return render(request,'tiendita/tienda/tienda.html',contexto)


#PRODUCTO
def bombo(request):
    return render(request,'tiendita/articulos/bombo.html')



#INICIO

def bienvenida(request):
    return render(request,'tiendita/inicio_sesion/bienvenida.html')

def inicio_sesion(resquest):
    return render(resquest, 'tiendita/inicio_sesion/inicio_sesion.html')

def nuevo_user(resquest):
    return render(resquest, 'tiendita/inicio_sesion/nuevo_user.html')

def restablecer(resquest):
    return render(resquest,'tiendita/inicio_sesion/restablecer.html')

def verificar(resquest):
    return render(resquest, 'tiendita/inicio_sesion/verificar.html')


#USUARIO

def actu_datos(resquest):
    return render(resquest, 'tiendita/usuario/actu_datos.html')

def carrito(resquest):
    return render(resquest, 'tiendita/usuario/carrito.html')

def histo_compra(resquest):
    return render (resquest, 'tiendita/usuario/histo_compra.html')

def mod_contra(resquest):
    return render (resquest, 'tiendita/usuario/mod_contra.html')


