from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    #ADMIN
    path('a_prod_nuevo/',a_prod_nuevo,name="a_prod_nuevo"),
    path('a_prod_agregar/',a_prod_agregar,name="a_prod_agregar"),
    path('a_prod_eliminar/',a_prod_eliminar,name="a_prod_eliminar"),
    #TIENDA
    path('',tienda,name="tienda"),
    path('prod_cuerda/',prod_cuerda,name="prod_cuerda"),
    path('prod_idiofono/',prod_idiofono,name="prod_idiofono"),
    path('prod_percusion/',prod_percusion,name="prod_percusion"),
    path('prod_viento/',prod_viento,name="prod_viento"),
    path('feriados/',feriados,name="feriados"),
    #PRODUCTO
    path('producto/<id>',producto,name="producto"),
    #INICIO
    path('bienvenida/',bienvenida,name="bienvenida"),
    path('cerrar_sesion/',cerrar_sesion,name="cerrar_sesion"),
    path('inicio_sesion/',inicio_sesion,name="inicio_sesion"),
    path('inicio_sesion_verificar/',inicio_sesion_verificar,name="inicio_sesion_verificar"),
    path('nuevo_user/',nuevo_user, name="nuevo_user"),
    path('nuevo_user_agregar/',nuevo_user_agregar, name="nuevo_user_agregar"),
    path('restablecer/',restablecer, name="restablecer"),
    path('verificar/',verificar, name="verificar"),
    path('verificar_agregar/',verificar_agregar, name="verificar_agregar"),
    #USUARIO
    path('actu_datos/',actu_datos,name="actu_datos"),
    path('carrito/', carrito, name="carrito"),
    path('histo_compra/', histo_compra, name= "histo_compra"),
    path('mod_contra/',mod_contra, name="mod_contra"),
]