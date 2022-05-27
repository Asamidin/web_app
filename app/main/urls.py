from django.urls import path
from .views import index, about, index1

urlpatterns = [
    path('index', index, name='index'),
    path('about', about, name='about'),
    path('index1', index1, name='index1')
]


