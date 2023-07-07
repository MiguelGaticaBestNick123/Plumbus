from django import forms
from django.contrib.auth.models import User
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    pass

            
class CustomUserCreationForm(UserCreationForm):
    pass
    class  Meta:
        model = User
        fields = ["username", "password1","password2"]

class FrmPagar(forms.ModelForm):
    class Meta: 
        fields = ("tipo_pago","nro_tarjeta","fecha_caducidad","titular")

class frmCrearCuenta(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email","first_name","last_name"]
# a

class frmContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "num_telefono", "asunto","descripcion"]
