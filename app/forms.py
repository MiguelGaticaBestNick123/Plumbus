from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "password"]
        
class CustomUserCreationForm(UserCreationForm):
    pass


class FrmPagar(forms.ModelForm):
    class Meta: 
        fields = ("tipo_pago","nro_tarjeta","fecha_caducidad","titular")

class frmCrearCuenta(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email","first_name","last_name"]
# a