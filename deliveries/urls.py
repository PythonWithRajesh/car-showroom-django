from django.urls import path
from . import views

urlpatterns = [

    path('', views.delivery_list, name='deliveries'),

    path('add/', views.add_delivery, name='add_delivery'),

]