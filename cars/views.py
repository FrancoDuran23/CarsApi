from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarSerializers
from .models import Car
from rest_framework import status
from django.http import Http404
from .serializers import *

class Car_APIView(APIView):
    serializer_class = CarSerializers
    def get(self, request, format=None, *args, **kwargs):
        cars = Car.objects.all()
        serializer = CarSerializers(cars, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CarSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Car_APIView_Detail(APIView):

    def get_object(self, pk):        
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializers(car)  
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializers(car, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CarsFilterSort_APIView(APIView):

    def get(self, request, filter_by, order_by, format=None):        
        match filter_by:
            case 0:   
                # Sin Filtro                  
                cars = Car.objects.all()
            case 1:
                # Filtrar por Autos
                cars = Car.objects.filter(vehicle_type=1)
            case 2:
                # Filtrar por Pickups and Comerciales
                cars = Car.objects.filter(vehicle_type__in=[2,3])
            case 3:
                # Filtrar por SUVs and Crossovers
                cars = Car.objects.filter(vehicle_type__in=[4,5])
        
        match order_by:
            case 1:
                # Ordenar Precio de Menor a Mayor
                cars = cars.order_by('price')
            case 2:
                # Ordenar Precio de Mayor a Menor
                cars = cars.order_by('-price')
            case 3:
                # Ordenar por Nuevos
                cars = cars.order_by('-year')            
            case 4:
                # Ordenar por Viejos
                cars = cars.order_by('year')        
                
        serializer = CarSerializers(cars, many=True) 
        return Response(serializer.data)



