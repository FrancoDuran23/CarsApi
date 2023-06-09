from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vehicle_type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, related_name='Brand',on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_type = models.ForeignKey(Vehicle_type, related_name='Brand', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='autos/')
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"