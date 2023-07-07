from django.urls import path
from .views import inicio, loginsexo, tienda, registro, logout_view, agregar_al_carrito, ver_carrito, eliminar_item_carrito


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', loginsexo, name="login"), 
    path('tienda', tienda, name="tienda"),
    path('registro/', registro, name="registro"),
    path('logout', logout_view, name="logout"),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar/<int:item_id>/', eliminar_item_carrito, name='eliminar_item_carrito'),   
]    
