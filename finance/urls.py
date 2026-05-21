from django.urls import path
from . import views

urlpatterns = [

    path('', views.finance_list, name='finance'),

    path('add/', views.add_finance, name='add_finance'),

]