from django.urls import path
from .views import create_album, edit_album
urlpatterns = [
    path('add/', create_album, name = "create_album" ), 
    path('edit/<int:id>', edit_album , name = "edit_album" ), 
]
