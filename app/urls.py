from django.urls import path
from .views import inicio, loginsexo, tienda, registro, logout_view


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', loginsexo, name="login"), 
    path('tienda', tienda, name="tienda"),
    path('registro/', registro, name="registro"),
    path('logout', logout_view, name="logout"),   
]    
