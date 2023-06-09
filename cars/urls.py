from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('api/cars', Car_APIView.as_view()), 
    path('api/cars/<int:pk>/', Car_APIView_Detail.as_view()),
    path('api/filter_and_sort/<int:filter_by>/<int:order_by>/', CarsFilterSort_APIView.as_view()),
    
]