from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Car, Brand, Vehicle_type

class CarsTest(TestCase):
    def setUp(self):
        # Crear una imagen de prueba
        imagen = SimpleUploadedFile(
            name='test_image.png',
            content=open('autos/imagen_2023-06-07_132425445.png', 'rb').read(),
            content_type='image/png'
        )

        #Crear instancias de Modelos Relacionados
        aux_brand = Brand.objects.create(name="Toyota")
        aux_type = Vehicle_type.objects.create(name="Autos")

        # Crear una instancia de Car con la clave foránea y la imagen
        self.car = Car.objects.create(
            brand=aux_brand,
            vehicle_type=aux_type,
            imagen=imagen,
            model='Corolla',
            year=2021,
            price=1900000,
        )

    def test_brand(self):
        # Obtener el modelo desde la base de datos
        car = Car.objects.get(id=self.car.id)

        # Verificar que el campo foráneo sea el esperado
        self.assertEqual(car.brand, self.car.brand)

    def test_type(self):
        # Obtener el modelo desde la base de datos
        car = Car.objects.get(id=self.car.id)

        # Verificar que el campo foráneo sea el esperado
        self.assertEqual(car.vehicle_type, self.car.vehicle_type)

    def test_imagen(self):
        # Obtener el modelo desde la base de datos
        car = Car.objects.get(id=self.car.id)

        # Verificar que la imagen sea igual a la imagen de prueba
        self.assertEqual(car.imagen.read(), self.car.imagen.read())
