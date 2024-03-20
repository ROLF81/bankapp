from django.urls import path
from .views import home, newMember, readMember

urlpatterns = [
    path ('', home, name= 'principal'),
    path ('add', newMember, name= 'agregar'),
    path ('leer', readMember, name= 'read')
]
