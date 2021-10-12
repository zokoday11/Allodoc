from django.db import models

from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.urls.conf import path
from django.contrib.auth.models import User

from django.dispatch import receiver 
from django.db.models.signals import post_save


########################### Classe utlitaire ###########################
class City(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Zip(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

########################### Section Docteurs ###########################

class Specialization(models.Model):
    specialization_name = models.CharField(max_length=100)
    def __str__(self):
        return self.specialization_name

# Modèle des docteurs
class Doctor(models.Model):
    SEX_CHOICES = [
        ('Masculin', 'M'),
        ('Feminin', 'F'),
    ]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='doctor')
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    specializations = models.ManyToManyField(Specialization, null=True, related_name='specializations')
    praticing_from = models.DateField(null=True)
    professional_statement = models.TextField(null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='Masculin', null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='doctors/%Y/%m/%d/', null=True)
    #password = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    #email = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    '''
    def get_absolute_url(self):
        return reverse('pages:doctor_detail', args=[self.id])           

    '''
# Modèle de qualification
class Qualification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='qualifications', null=True)
    qualification_name = models.CharField(max_length=200, null=True)
    institute_name = models.CharField(max_length=200, null=True)
    procurement_year = models.DateField(null=True)
    def __str__(self):
        return self.qualification_name

class DoctorAvailibity(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availibities', null=True)
    name = models.CharField(max_length=100, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    is_reserved = models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.name