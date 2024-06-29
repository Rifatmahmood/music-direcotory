from django.urls import path
from .views import musician_list, create_musician, musician_update, musician_delete


urlpatterns = [

    path('add/', create_musician, name='musician_create'  ), 
    path('update/<int:id>/', musician_update, name='musician_update'),
    path('delete/<int:id>/', musician_delete, name='musician_delete'),
    
]
