from django.urls import path
from api_rest.views import lista_comuna, lista_region,lista_region_id,lista_comuna_id

urlpatterns = [
    path('lista_comuna/',lista_comuna,name="lista_comuna"),
    path('lista_region/',lista_region,name="lista_region"),
    path('lista_region_id/<id>',lista_region_id,name="lista_region_id"),
    path('lista_comuna_id/<id>',lista_comuna_id,name="lista_comuna_id"),
]