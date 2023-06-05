from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from tiendita.models import Region, Comuna
from .serializers import comunaSerializers,regionSerializers
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def lista_region(request):
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = regionSerializers(region, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = regionSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
