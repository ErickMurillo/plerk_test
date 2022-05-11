from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [
    path('resumen/',servicio_resumen),
    path('empresa/<id>',servicio_empresa),
]