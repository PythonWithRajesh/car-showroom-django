from django.urls import path
from . import views

urlpatterns = [

    path('', views.car_list, name='cars'),

    path('add/', views.add_car, name='add_car'),

]