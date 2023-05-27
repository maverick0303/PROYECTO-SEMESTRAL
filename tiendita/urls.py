from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    #TIENDA
    path('',tienda,name="tienda"),
    path('bombo/',bombo,name="bombo"),
    path('a_bombo/',a_bombo,name="a_bombo"),
    path('a_prod_cuerda/',a_prod_cuerda,name="a_prod_cuerda"),
    path('a_prod_idiofono/',a_prod_idiofono,name="a_prod_idiofono"),
    path('a_prod_percusion/',a_prod_percusion,name="a_prod_percusion"),
    path('a_prod_viento/',a_prod_viento,name="a_prod_viento"),
    path('a_prod_nuevo/',a_prod_nuevo,name="a_prod_nuevo"),
    path('a_prod_agregar/',a_prod_agregar,name="a_prod_agregar"),
    path('a_tienda/',a_tienda,name="a_tienda"),
    path('prod_cuerda/',prod_cuerda,name="prod_cuerda"),
    path('prod_idiofono/',prod_idiofono,name="prod_idiofono"),
    path('prod_percusion/',prod_percusion,name="prod_percusion"),
    path('prod_viento/',prod_viento,name="prod_viento"),
    path('feriados/',feriados,name="feriados"),
    #INICIO
    path('bienvenida/',bienvenida,name="bienvenida"),
    path('inicio_sesion/',inicio_sesion,name="inicio_sesion"),
    path('nuevo_user/',nuevo_user, name="nuevo_user"),
    path('restablecer/',restablecer, name="restablecer"),
    path('verificar/',verificar, name="verificar"),
    #USUARIO
    path('actu_datos/',actu_datos,name="actu_datos"),
    path('carrito/', carrito, name="carrito"),
    path('histo_compra/', histo_compra, name= "histo_compra"),
    path('mod_contra/',mod_contra, name="mod_contra"),
]