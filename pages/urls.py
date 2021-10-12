
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
     #Login views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #Vue d'inscription
    path('doctor-signup/', views.doctor_signup, name='doctor_signup'),
    #Vues des informations des docteurs
    path('list/', views.doctor_list, name='doctor_list'),
    path('list-grid/', views.doctor_list_grid, name='doctor_list_grid'),
    path('<first_name>/<last_name>/', views.doctor, name='doctor_detail'),
    path('doctor-profile/', views.doctor_profile, name='doctor_profile'),
    path('<int:id>/', views.doctor_detail, name='doctor_detail'),
    #Vues sur les activitiés et formations des docteurs 
    path('doctor-new-qualification/', views.doctor_qualification, name='doctor_qualification'),
    path('doctor-formations/', views.doctor_formations, name='doctor_formations'),
    path('doctor-availability/', views.doctor_availability, name='doctor_availability'),
    #Vues d'informations du site
    path('contact-us/', views.contact_us, name='contact_us'),
    path('help/', views.faq, name='faq'),
    #Vues des rendez-vous
    path('appointment/<int:id>/<name>/', views.booking, name='appointment'),
    path('appointments/', views.appointments, name='appointments'),
    path('availabilities/', views.availabilities, name='availabilities'), 
]