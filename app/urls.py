from django.urls import path
from .views import inicio, loginsexo


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', loginsexo, name="login"),    

]    
