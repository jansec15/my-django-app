from django.contrib import admin
from .models import Paciente,TipoIdentificacion
# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    list_display= ('numero_identificacion','nombre','apellido')

class TipoIdAdmin(admin.ModelAdmin):
    list_display= ('acronimo','nombre')

admin.site.register(Paciente,PacienteAdmin)
admin.site.register(TipoIdentificacion,TipoIdAdmin)

