from django.contrib import admin
from .models import Planta, Producto, RegistroProduccion, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Planta)
admin.site.register(Producto)
admin.site.register(RegistroProduccion)
