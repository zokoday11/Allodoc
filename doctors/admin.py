from typing import ChainMap
from django.contrib import admin
from django.db import models

from .models import Specialization, Doctor, Qualification, City, State, Zip, DoctorAvailibity


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Zip)
class ZipAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'praticing_from', 'sex', 'created', 'photo']


@admin.register(DoctorAvailibity)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'start_date', 'end_date']


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['specialization_name']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['institute_name', 'procurement_year']


