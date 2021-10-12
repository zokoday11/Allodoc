from django.db import models

from django.contrib.admin.decorators import register
from django.db import models


from doctors.models import City, Zip, State

class Patient(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=150, null=True)
    photo = models.ImageField(upload_to='patients/%Y/%m/%d/', null=True)
    street = models.CharField(max_length=200,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.first_name
