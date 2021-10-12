from pages.models import Appointment
from django.http import HttpResponse
from django.core import paginator
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls.conf import path
from doctors.models import Doctor, Qualification, Specialization, DoctorAvailibity
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, QualificationForm, DoctorAvailibityForm, PatientForm

# Section page d'acceuil
def index(request):
    some_doctors = Doctor.objects.all()[:4]
    return render(request, 'Home/index.html', {'some_doctors': some_doctors})

# Section docteur
def doctor_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        object_list = Doctor.objects.order_by('-created').filter(professional_statement=search_query)
    else:
        object_list = Doctor.objects.order_by('-created')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, délivrer la première page
        doctors = paginator.page(1)
    except EmptyPage:
        # Si la page est au dela de l'intervalle, delivrer la dernière page des résultats
        doctors = paginator.page(page.num_pages)       
    return render(request, 'Details/list.html', {'page': page, 'doctors': doctors})

def doctor_list_grid(request):
    object_list = Doctor.objects.order_by('-created')
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, délivrer la première page
        doctors = paginator.page(1)
    except EmptyPage:
        # Si la page est au dela de l'intervalle, delivrer la dernière page des résultats
        doctors = paginator.page(page.num_pages)       
    return render(request, 'Details/grid-list.html', {'page': page, 'doctors': doctors})


def doctor(request, first_name, last_name):
    return render(request, "Details/doctor.html")

def doctor_detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    qualifications = Qualification.objects.filter(doctor=doctor)
    availibities = DoctorAvailibity.objects.filter(doctor=doctor)
    return render(request, 'Details/doctor.html', {'doctor': doctor, 'qualifications': qualifications, 'availibities': availibities})

def doctor_signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # Save the User object
            new_user.save()
            Doctor.objects.create(user=new_user)
            return render(request, 'Welcome/welcome_user.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'Signup/register-doctor-working.html', {'user_form': user_form})            

@login_required
def doctor_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.doctor, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile mise à jour avec succès')
        else:
            messages.error(request, 'Erreur des mises à jour de votre profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.doctor)
    return render(request, 'Admin/doctor-profile.html', {'user_form': user_form, 'profile_form': profile_form})                   


@login_required
def doctor_qualification(request):
    if request.method == 'POST':
        qualification_form = QualificationForm(data=request.POST)
        if qualification_form.is_valid():
            diplome = qualification_form.save(commit=False)
            diplome.doctor = request.user.doctor
            diplome.save()
            messages.success(request, 'Formation ajoutée avec succès')
            return redirect('pages:doctor_formations')
        else:
            messages.error(request, 'Erreur d\'ajout de formation')
    else:
        qualification_form = QualificationForm()
    return render(request, 'Admin/doctor-formation.html', {'qualification_form': qualification_form})                

@login_required
def doctor_formations(request):
    formations = Qualification.objects.filter(doctor=request.user.doctor)
    return render(request, 'Admin/doctor-formations.html', {'formations': formations})   

@login_required
def doctor_availability(request):
    if request.method == 'POST':
        doctor_availibity_form = DoctorAvailibityForm(data=request.POST)
        if doctor_availibity_form.is_valid():
            instance = doctor_availibity_form.save(commit=False)
            instance.doctor = request.user.doctor
            instance.save()
            messages.success(request, 'Disponibilité ajoutée avec succès')
        else:
            messages.error(request, 'Erreur d\'ajout de disponibilité')
    else:
        doctor_availibity_form = DoctorAvailibityForm()            
    return render(request, "Admin/new_avaibiity.html", {'doctor_availibity_form':doctor_availibity_form})

# Section Booking ou réservation
def appointment(request):
    pass

#Section contact
def contact_us(request):
    return render(request,'Contact/contacts.html')

# Section FAQ
def faq(request):
    return render(request, 'faq/faq.html')

#Section patient

#Section Renez-vous
def appointment(request, id):
    patient_form = PatientForm()
    return render(request, 'Details/new-booking.html', {'patient_form':patient_form})

def booking(request, id, name):
    doctor = Doctor.objects.get(user__first_name=name)
    availibity = DoctorAvailibity.objects.get(id=id)
    availibity.is_reserved = False
    availibity.save()
    if request.method == 'POST':
        patient_form = PatientForm(data=request.POST)
        if patient_form.is_valid():
            patient = patient_form.save(commit=False)
            start_date = availibity.start_date
            end_date = availibity.end_date
            patient.save()
            Appointment.objects.create(doctor=doctor, patient=patient, start_date=start_date, end_date=end_date)
            return render(request, 'Welcome/reservation.html')
    else:
        patient_form = PatientForm()
    return render(request, 'Details/new-booking.html', {'patient_form':patient_form, 'doctor': doctor, 'availibity': availibity})

def booking_confirmation(request):
    return render(request, 'Welcome/confirm1.html')

@login_required
def appointments(request):
    appointments = Appointment.objects.filter(doctor=request.user.doctor)
    return render(request, 'Admin/appointments.html', {'appointments': appointments})

@login_required
def availabilities(request):
    availabilities = DoctorAvailibity.objects.filter(doctor=request.user.doctor)
    return render(request, 'Admin/availabilities.html', {'availabilities': availabilities})