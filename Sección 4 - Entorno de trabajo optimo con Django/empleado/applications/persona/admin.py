from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
    'first_name',
    'last_name',
    'job',
    )


admin.site.register(Empleado, EmpleadoAdmin)
