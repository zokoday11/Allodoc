from django.contrib import admin

from .models import Appointment

@admin.register(Appointment)
class AppoimentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient']