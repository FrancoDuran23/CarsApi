from django.contrib import admin
from .models import Brand, Car, Vehicle_type

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'vehicle_type')
    list_filter = ('brand', 'year')
    search_fields = ('brand__name', 'model', 'vehicle_type__name')

admin.site.register(Brand)
admin.site.register(Car, CarAdmin)
admin.site.register(Vehicle_type)
