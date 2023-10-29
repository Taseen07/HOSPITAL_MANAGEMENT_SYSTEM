"""
URL configuration for the Hospital project.

"""

# Importing required modules
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from homepage import views

# URL patterns for the Hospital project
urlpatterns = [
    # Path for the admin site
    path('admin/', admin.site.urls, name='admin'),

    # Path for the home screen view
    path('', views.home_screen_view, name='home_screen_view'),

    # Path for the login view
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Path for the logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Path for the register doctor view
    path('register/doctor/', views.register_doctor, name='register_doctor'),

    # Path for the register patient view
    path('register/patient/', views.register_patient, name='register_patient'),

    # Path for the dashboard view
    path('dashboard/', views.dashboard, name='dashboard'),

    # Path for the search view
    path('search/', views.search, name='search'),

    # Path for the doctor detail view
    path('doctor/<str:username>/', views.doctor_detail, name='doctor_detail'),

    # Path for the Terms & Conditions page
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),

    # Path for the Privacy Policy page
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

    # Path for the About Us page
    path('about_us/', views.about_us, name='about_us'),

    # Path for the Services page
    path('services/', views.services, name='services'),

    # Path for the Emergency Services page
    path('emergency_services/', views.emergency_services, name='emergency_services'),

    # Path for the Doctors List page
    path('doctors/', views.doctors, name='doctors'),

    # Path for the Staff page
    path('staff/', views.staff, name='staff'),

    # Path for the Blood Bank page
    path('blood_bank/', views.blood_bank, name='blood_bank'),

    # Path for the bed reservation page
    path('bed_reservation/', views.bed_reservation, name='bed_reservation'),

    # Path for booking a doctor's appointment
    path('doctor/<str:username>/book_doctor_appointment/',
         views.book_doctor_appointment, name='book_doctor_appointment'),

    # Path for the successful booking of doctor's appointment
    path('doctor/<str:username>/appointment_confirmation/',
         views.doctor_appointment_confirmation, name='doctor_appointment_confirmation'),
]
