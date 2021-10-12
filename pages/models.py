from django.db import models
from doctors.models import Doctor
from patients.models import Patient


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(null=True)
    start_date = models.DateTimeField(null=True)