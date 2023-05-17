from django.contrib import admin
from django.urls import path, include
from .views import (tienda,bombo,a_bombo,a_prod_cuerda,a_prod_idiofono,a_prod_percusion,
                    a_prod_viento,a_prod_nuevo,a_tienda,prod_cuerda,prod_idiofono,prod_percusion,prod_viento,feriados)
urlpatterns = [
    path('',tienda,name="tienda"),
    path('bombo/',bombo,name="bombo"),
    path('a_bombo/',a_bombo,name="a_bombo"),
    path('a_prod_cuerda/',a_prod_cuerda,name="a_prod_cuerda"),
    path('a_prod_idiofono/',a_prod_idiofono,name="a_prod_idiofono"),
    path('a_prod_percusion/',a_prod_percusion,name="a_prod_percusion"),
    path('a_prod_viento/',a_prod_viento,name="a_prod_viento"),
    path('a_prod_nuevo/',a_prod_nuevo,name="a_prod_nuevo"),
    path('a_tienda/',a_tienda,name="a_tienda"),
    path('prod_cuerda/',prod_cuerda,name="prod_cuerda"),
    path('prod_idiofono/',prod_idiofono,name="prod_idiofono"),
    path('prod_percusion/',prod_percusion,name="prod_percusion"),
    path('prod_viento/',prod_viento,name="prod_viento"),
    path('feriados/',feriados,name="feriados"),
]