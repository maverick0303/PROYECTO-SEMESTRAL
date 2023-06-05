from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from tiendita.models import Comuna, Region
from .serializers import comunaSerializers, regionSerializers
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_comuna(request):
    if request.method == 'GET':
        comuna = Comuna.objects.all()
        serializer = comunaSerializers(comuna, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = comunaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_region(request):
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = regionSerializers(region, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = regionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
