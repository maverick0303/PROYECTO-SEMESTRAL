from django.shortcuts import render

# Create your views here.
def bombo(request):
    return render(request,'tiendita/articulos/bombo.html')

def tienda(request):
    nombre="Leo"
    contexto = {
        "nomb":nombre
    }
    return render(request,'tiendita/tienda/tienda.html',contexto)