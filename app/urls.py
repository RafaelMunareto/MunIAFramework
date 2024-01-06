from django.urls import path
from .controller import app

urlpatterns = [
    path('', app.index, name='index'),
]
