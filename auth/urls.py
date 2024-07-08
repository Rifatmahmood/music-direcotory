from django.urls import path
from .views import signup, user_login, user_logout
urlpatterns = [

    path('signup/', signup, name='signup_page'  ), 
    path('login/', user_login, name='login_page'),
    path('logout/', user_logout, name='logout'),
  
    
]
