from django.contrib import admin
from .models import PlumbusX, Plumbus, Carrito, Pedido, Universo, Galaxia, Planeta, FormularioPago, Contacto, Producto, ItemCarrito

class PlumbusXAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "largo_dingle_dop", "vibracion_floops", "grodus_inalambrico", "imagen")
    list_editable = ("nombre", "precio", "largo_dingle_dop", "vibracion_floops", "grodus_inalambrico")
    list_display_links = None

    class Meta:
        model = PlumbusX

class PlumbusAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "f_creacion", "f_caducidad", "c_chumbles", "imagen")
    list_editable = ("nombre", "precio", "f_creacion", "f_caducidad", "c_chumbles")
    list_display_links = None

    class Meta:
        model = Plumbus

class CarritoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "plumbus", "plumbusX", "cantidad")

    class Meta:
        model = Carrito

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("fecha_creacion", "estado", "direccion_envio")
    list_editable = ("estado", "direccion_envio")

    class Meta:
        model = Pedido

class UniversoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

    class Meta:
        model = Universo

class GalaxiaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

    class Meta:
        model = Galaxia

class PlanetaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

    class Meta:
        model = Planeta

class FormularioPagoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nombre_titular", "numero_tarjeta", "monto_total", "fecha_creacion", "direccion_envio", "galaxia_envio", "planeta_envio", "codigo_postal")
    list_editable = ("nombre_titular", "direccion_envio", "galaxia_envio", "planeta_envio", "codigo_postal")

    class Meta:
        model = FormularioPago
        
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "num_telefono", "asunto","descripcion")
    class Meta:
        model = Contacto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    
    class Meta:
        model = Producto

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ("producto", "cantidad", "usuario")
    class Meta:
        model = ItemCarrito

admin.site.register(PlumbusX, PlumbusXAdmin)
admin.site.register(Plumbus, PlumbusAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Universo, UniversoAdmin)
admin.site.register(Galaxia, GalaxiaAdmin)
admin.site.register(Planeta, PlanetaAdmin)
admin.site.register(FormularioPago, FormularioPagoAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ItemCarrito, ItemCarritoAdmin)