
from django.urls import path
from .views import *

urlpatterns = [
    path("crearPariente/", crearPariente, name ="parientes"),
]
