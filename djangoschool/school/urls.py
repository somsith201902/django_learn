from django.urls import path
from .views import *
urlpatterns = [
    #localhost:8000/
    path('', HomePage)
]