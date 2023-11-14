from django.urls import path
from .views import beranda,index

urlpatterns = [
    path('', beranda, name='beranda.html'),
    path('', index, name='index.html'),
]