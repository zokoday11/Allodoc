
from django import forms
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import fields, models, widgets
from doctors.models import Doctor, City, State, Zip, Qualification, DoctorAvailibity, Specialization

from patients.models import Patient

# Formulaires réliés aux inscriptions et aux profiles des medécins

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Votre mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Votre mot de passe à nouveau', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email')
        labels = {'username':'Nom d\'utilisateur', 'first_name': 'Prénom(s)', 'last_name':'Nom(s)', 'email': 'Adresse mail'}
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Les mots de passe ne correpondent pas.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {'username': 'Nom d\'utilisateur','first_name': 'Prénom(s)', 'last_name': 'Nom(s)', 'email':'Adresse mail'}

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('specializations', 'praticing_from', 'professional_statement', 'sex', 'photo', 'phone', 'street', 'zip', 'state', 'city')
        labels = {'specializations':'Spécialisation(s)', 'praticing_from': 'Date de début', 'sex':'Sexe', 'photo': 'Image de profil','phone':'Numéro de téléphone', 'street':'Rue', 'zip':'Code postal', 'state':'Département','city':'Ville'}
        widgets = {
            'practicing_form': forms.DateField(),
        }

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ('qualification_name','institute_name', 'procurement_year')
        labels = {'qualification_name':'Nom du diplôme','institute_name':'Nom de l\'institut', 'procurement_year':'Date de l\'obtention'}
        widgets = {'procurement_year': forms.SelectDateWidget()}
class DoctorAvailibityForm(forms.ModelForm):
    class Meta:
        model = DoctorAvailibity
        fields = ('name','start_date', 'end_date')
        labels = {'name':'Nom','start_date':'Date de début','end_date':'Date de fin'}
        widgets = {'start_date': forms.SelectDateWidget()}

#Formulaires du patient
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'email', 'phone', 'photo', 'street', 'zip', 'state', 'city')
        labels = {'first_name':'Prénom(s)', 'last_name':'Nom(s)', 'email': 'Votre addresse mail', 'phone':'Numéro de téléphone', 'photo':'Image', 'street':'Rue','zip':'Code postal','state':'Département','city':'Ville'}