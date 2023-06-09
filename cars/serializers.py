from rest_framework import serializers 
from .models import Car, Vehicle_type, Brand
from PIL import Image

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_type
        fields = ['name']

class CarSerializers(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset= Brand.objects.all(), source='brand.name')
    model = serializers.CharField(label="Ingrese Nombre de Modelo",max_length=100)
    year = serializers.IntegerField(label="Ingrese Año de Fabricación")
    price = serializers.DecimalField(label="Ingrese Precio",max_digits=10, decimal_places=2)
    vehicle_type = serializers.PrimaryKeyRelatedField(queryset= Vehicle_type.objects.all(), source='vehicle_type.name')
    imagen = serializers.ImageField(label="Agregue Imagen")

    def validate_imagen(self, imagen):
        # Validar el tamaño de la imagen si es necesario
        max_size = (1024, 1024)  # Tamaño máximo permitido (ancho, alto)        
        image = Image.open(imagen)
        
        if image.size > max_size:
            raise serializers.ValidationError("La imagen supera el tamaño máximo permitido.")

        return imagen
    
    class Meta:
        model = Car
        fields = ['brand','model', 'year', 'price', 'vehicle_type', 'imagen']


