from django.db import models
from django.contrib.auth.models import User


CANTIDAD_CHUMBLES = [
    ("KC°", "KC°"),
    ("%Z", "%Z"),
    ("O", "O"),
    ("O)", "O)"),
]
CANTIDAD = [
    ("1" , "1"),
    ("2" , "2"),
    ("3" , "3"),
    ("4" , "4"),
    ("5" , "5"),
    ("6" , "6"),
    ("7" , "7"),
    ("8" , "8"),
    ("9" , "9"),
    ("10" , "10"),
]

ESTADO = [
    ('PENDIENTE', 'Pendiente'),
    ('EN_PROCESO', 'En proceso'),
    ('ENVIADO', 'Enviado'),
    ('ENTREGADO', 'Entregado'),
    ('CANCELADO', 'Cancelado'),
    ('DEVUELTO', 'Devuelto'),
]
# Create your models here.
# Usuario, el cliente  (DELETED)

#Colocamos los pumblus que es lo segundo más importante


class PlumbusX(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    largo_dingle_dop = models.DecimalField(max_digits=5, decimal_places=2)
    vibracion_floops = models.IntegerField()
    grodus_inalambrico = models.BooleanField()
    imagen= models.ImageField(upload_to='productos') 
    def __str__(self):
        return self.nombre 


class Plumbus (models.Model):
    nombre=models.CharField(max_length=50, null=False)
    precio= models.IntegerField(null=False)
    f_creacion=models.DateField()
    f_caducidad=models.DateField()
    c_chumbles=models.CharField(choices=CANTIDAD_CHUMBLES, max_length=10)
    imagen= models.ImageField(upload_to="productos", null=True)  
    
    def __str__(self):
        return self.nombre 
    
#Carrito y productoss


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    plumbus = models.ForeignKey(Plumbus, on_delete=models.CASCADE, null=True)
    plumbusX = models.ForeignKey(PlumbusX, on_delete=models.CASCADE, null=True)
    cantidad=models.CharField(choices=CANTIDAD, max_length=2)    
    
    def subtotal(self):
        if self.plumbus:
            return self.plumbus.precio * self.cantidad
        elif self.plumbusX:
            return self.plumbusX.precio * self.cantidad
        else:
            return 0


class Pedido(models.Model):
    carrito = models.ManyToManyField(Carrito)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(choices=ESTADO,max_length=15, default='Pendiente')
    direccion_envio = models.CharField(max_length=150)
    
class Universo (models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre 
    
class Galaxia (models.Model):
    
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre 
    
class Planeta (models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre 
    
    

class FormularioPago(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_titular = models.CharField(max_length=100)
    numero_tarjeta = models.CharField(max_length=16)
    fecha_expiracion = models.DateField()
    codigo_seguridad = models.CharField(max_length=4)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Detalles de envío
    direccion_envio = models.CharField(max_length=150)
    universo_envio = models.ForeignKey(Universo, on_delete=models.CASCADE, default=1)
    galaxia_envio = models.ForeignKey(Galaxia, on_delete=models.CASCADE)
    planeta_envio = models.ForeignKey(Planeta, on_delete=models.CASCADE)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"Formulario de Pago creado el {self.fecha_creacion}"

class Contacto(models.Model):
        nombre = models.CharField(max_length=100, null=False)
        correo = models.EmailField(null=False)
        num_telefono = models.CharField(max_length=20, null=True)
        asunto = models.CharField(max_length=80, null=False, default="n/a")
        descripcion = models.TextField(null=False)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
