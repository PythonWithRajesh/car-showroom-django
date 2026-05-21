from django.urls import path
from . import views


urlpatterns = [

    path('', views.followup_list,
        name='followups'),

    path('add/',
        views.add_followup,
        name='add_followup'),

]