from django.urls import path
# from .views import create_album, edit_album
from .views import CreateAlbumView, EditAlbumView
# urlpatterns = [
#     path('add/', create_album, name = "create_album" ), 
#     path('edit/<int:id>', edit_album , name = "edit_album" ), 
# ]
urlpatterns = [
    path('create_album/', CreateAlbumView.as_view(), name='create_album'),
    path('edit_album/<int:id>/', EditAlbumView.as_view(), name='edit_album'),
]