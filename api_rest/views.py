from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from tiendita.models import Comuna, Region
from .serializers import comunaSerializers, regionSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
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
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def lista_comuna_id(request, id):
    try:
        comuna = Comuna.objects.get(id_comuna = id)
    except Region.DoesNotExist:
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = comunaSerializers(comuna)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = comunaSerializers(comuna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comuna.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
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

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def lista_region_id(request, id):
    try:
        region = Region.objects.get(id_region = id)
    except Region.DoesNotExist:
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = regionSerializers(region)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = regionSerializers(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        region.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

