from django.urls import path
from api_rest.views import lista_comuna, lista_region

urlpatterns = [
    path('lista_comuna/',lista_comuna,name="lista_comuna"),
    path('lista_region/',lista_region,name="lista_region"),
]