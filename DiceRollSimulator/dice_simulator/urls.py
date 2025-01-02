from django.urls import path
from . import views

urlpatterns = [
    path('', views.roll_dice, name='roll_dice'),
]
