from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    model = Local
    list_display = ('nombre', 'direccion', 'telefono')
