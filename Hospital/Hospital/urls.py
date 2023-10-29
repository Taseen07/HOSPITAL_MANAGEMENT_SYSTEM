"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from homepage import views
from bedReserve import views as bedReserveViews

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Home screen view
    path('', views.home_screen_view, name='home_screen_view'),

    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Register doctor view
    path('register/doctor/', views.register_doctor, name='register_doctor'),

    # Register patient view
    path('register/patient/', views.register_patient, name='register_patient'),

    # Dashboard view
    path('dashboard/', views.dashboard, name='dashboard'),

    # Search view
    path('search/', views.search, name='search'),

    # Doctor detail view
    path('doctor/<str:username>/', views.doctor_detail, name='doctor_detail'),

    # Terms & Conditions page
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),

    # Privacy Policy page
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

    # About Us page
    path('about_us/', views.about_us, name='about_us'),

    # Services page
    path('services/', views.services, name='services'),

    # Emergency-services page
    path('emergency-services/', views.emergency_services, name='emergency_services'),

    # Doctor's List page
    path('doctors/', views.doctors, name='doctors'),

    # Staff page
    path('staff/', views.staff, name='staff'),

    # Blood Bank page
    path('blood-bank/', views.blood_bank, name='blood_bank'),

    # Other Services page
    path('bed_reservation/', views.bed_reservation, name='bed_reservation'),

    # Other Services page
    path('bed_reservation/extensive_bed_search/', bedReserveViews.extensive_bed_search, name='extensive_bed_search'),

    # General Bed Search page
    path('bed_reservation/general_bed_search/', bedReserveViews.general_bed_search, name='general_bed_search'),
]
