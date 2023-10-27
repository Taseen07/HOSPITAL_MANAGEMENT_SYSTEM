# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms.models import inlineformset_factory
from .forms import UserRegistrationForm, DoctorForm, PatientForm, TimingForm, DoctorSearchForm
from .models import Doctor, Timing


def login_view(request):
    """
    Handle user login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin/') if user.is_superuser else redirect('dashboard')

    return render(request, 'homepage/login.html')


def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    return redirect('home_screen_view')


def register_doctor(request):
   """
   Handle doctor registration.
   """
   TimingFormSet = inlineformset_factory(Doctor, Timing, form=TimingForm, extra=1)

   if request.method == 'POST':
       user_form = UserRegistrationForm(request.POST)
       doctor_form = DoctorForm(request.POST, request.FILES)
       formset = TimingFormSet(request.POST)

       if user_form.is_valid() and doctor_form.is_valid() and formset.is_valid():
           user = user_form.save()
           doctor = doctor_form.save(commit=False)
           doctor.user = user
           doctor.save()
           instances = formset.save(commit=False)
           for instance in instances:
               instance.doctor = doctor
               instance.save()
           return redirect('login')
   else:
       user_form = UserRegistrationForm()
       doctor_form = DoctorForm()
       formset = TimingFormSet()

   return render(request, 'register_doctor.html', {'user_form': user_form, 'doctor_form': doctor_form, 'formset': formset})


def register_patient(request):
    """
    Handle patient registration.
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        patient_form = PatientForm(request.POST, request.FILES)

        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        patient_form = PatientForm()

    return render(request, 'register_patient.html', {'user_form': user_form, 'patient_form': patient_form})


def dashboard(request):
    """
    Render the dashboard view.
    """
    return render(request, 'dashboard.html', {'user': request.user})


def home_screen_view(request):
    """
    Render the home screen view.
    """
    return render(request, "homepage/homepage.html")


def search(request):
    """
    Handle the form submission and search for doctors.
    The search term is matched with both the first name and last name of the doctors.
    If no doctors are found, an error message is displayed.
    """
    if request.method == "POST":
        form = DoctorSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            search_terms = search_term.split()
            if len(search_terms) > 1:
                # If there are two or more words in the search term,
                # assume the first word is the first name and the second word is the last name.
                doctors = Doctor.objects.filter(user__first_name__icontains=search_terms[0],
                                                user__last_name__icontains=search_terms[1])
            else:
                # If there's only one word in the search term,
                # match it with either the first name or the last name.
                doctors = Doctor.objects.filter(user__first_name__icontains=search_term) | \
                           Doctor.objects.filter(user__last_name__icontains=search_term)
            if not doctors:
                return render(request, 'search_doctor.html', {'error_message': 'No doctor found'})
            return render(request, 'search_doctor.html', {'doctors': doctors})
    else:
        form = DoctorSearchForm()
    return render(request, "homepage/homepage.html")
def doctor_detail(request, username):
    """Display details for a specific doctor."""
    doctor = Doctor.objects.get(user__username=username)
    return render(request, 'doctor_detail.html', {'doctor': doctor})