from django.urls import path
from .views import inicio, loginsexo, tienda


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', loginsexo, name="login"), 
    path('tienda', tienda, name="tienda"),   

]    
