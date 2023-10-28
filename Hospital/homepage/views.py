# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms.models import inlineformset_factory
from .forms import UserRegistrationForm, DoctorForm, PatientForm, TimingForm, DoctorSearchForm, AppointmentForm
from .models import Doctor, Timing, Patient
from django.utils import timezone


def login_view(request):
    """
    Handle user login.

    This view handles the POST request for user login. It authenticates the user
    using the provided username and password. If the authentication is successful,
    it logs in the user and redirects them to the appropriate page based on their
    user type. If the user is a superuser, they are redirected to the admin page.
    Otherwise, they are redirected to the dashboard.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response. If the request method is POST and the user is
                  authenticated, it redirects to the appropriate page. Otherwise,
                  it renders the login page.
    """

    # Check if the request method is POST
    if request.method == 'POST':
        # Get username and password from POST data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # If user is authenticated
        if user is not None:
            # Log in user
            login(request, user)

            # Determine redirect URL based on whether user is superuser
            next_url = '/admin/' if user.is_superuser else 'dashboard'

            # Redirect to determined URL
            return redirect(next_url)

    # If request method is not POST or user is not authenticated, render login page
    return render(request, 'homepage/login.html')


def logout_view(request):
    """
    Log out the user and redirect them to the home screen view.

    This view logs out the user using Django's logout() function, then redirects
    them to the home screen view.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponseRedirect: An HTTP response that redirects to the home screen view.
    """
    logout(request)
    return redirect('home_screen_view')


def register_doctor(request):
    """
    Handle doctor registration.

    This view handles the POST request for doctor registration. It creates and validates
    a UserRegistrationForm, a DoctorForm, and a TimingFormSet. If all forms are valid,
    it saves the user and doctor instances, associates each timing instance with the doctor,
    and saves them. Then it redirects to the login page.

    If the request method is not POST or if any form is not valid, it renders the
    register_doctor.html template with the forms.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response. If the request method is POST and all forms are valid,
                  it redirects to the login page. Otherwise, it renders the register_doctor.html
                  template with the forms.
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

    return render(request, 'register_doctor.html',
                  {'user_form': user_form, 'doctor_form': doctor_form, 'formset': formset})


def register_patient(request):
    """
    Handle patient registration.

    This view handles the POST request for patient registration. It creates and validates
    a UserRegistrationForm and a PatientForm. If both forms are valid, it saves the user
    and patient instances and redirects to the login page.

    If the request method is not POST or if any form is not valid, it renders the
    register_patient.html template with the forms.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response. If the request method is POST and both forms are valid,
                  it redirects to the login page. Otherwise, it renders the register_patient.html
                  template with the forms.
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

   This view renders the dashboard.html template with the current user as context.

   Parameters:
   request (HttpRequest): The HTTP request object.

   Returns:
   HttpResponse: The HTTP response that renders the dashboard.html template.
   """
    return render(request, 'dashboard.html', {'user': request.user})


def home_screen_view(request):
    """
   Render the home screen view.

   This view renders the homepage/homepage.html template.

   Parameters:
   request (HttpRequest): The HTTP request object.

   Returns:
   HttpResponse: The HTTP response that renders the homepage/homepage.html template.
   """
    return render(request, "homepage/homepage.html")


def search(request):
    """
    Handle the form submission and search for doctors.

    This view handles the POST request for searching doctors. It creates and validates
    a DoctorSearchForm. If the form is valid, it splits the search term into words and
    matches them with the first name and last name of the doctors. If no doctors are found,
    it renders the search_doctor.html template with an error message. Otherwise, it renders
    the same template with the found doctors.

    If the request method is not POST or if the form is not valid, it renders the
    homepage/homepage.html template.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response. If the request method is POST and the form is valid,
                  it renders the search_doctor.html template with either an error message
                  or the found doctors. Otherwise, it renders the homepage/homepage.html
                  template.
    """
    if request.method == "POST":
        form = DoctorSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            search_terms = search_term.split()
            if len(search_terms) > 1:
                doctors = Doctor.objects.filter(user__first_name__icontains=search_terms[0],
                                                user__last_name__icontains=search_terms[1])
            else:
                doctors = Doctor.objects.filter(user__first_name__icontains=search_term) | \
                          Doctor.objects.filter(user__last_name__icontains=search_term)
            if not doctors:
                return render(request, 'search_doctor.html', {'error_message': 'No doctor found'})
            return render(request, 'search_doctor.html', {'doctors': doctors})
    else:
        form = DoctorSearchForm()
    return render(request, "homepage/homepage.html")


def doctor_detail(request, username):
    """
    Display details for a specific doctor.

    This view gets a Doctor object by username and renders the doctor_detail.html template
    with this doctor as context.

    Parameters:
    request (HttpRequest): The HTTP request object.
    username (str): The username of the doctor.

    Returns:
    HttpResponse: The HTTP response that renders the doctor_detail.html template.
    """
    doctor = Doctor.objects.get(user__username=username)
    return render(request, 'doctor_detail.html',
        {'doctor': doctor, 'username': doctor.user.username})


from django.utils import timezone


def book_doctor_appointment(request, username):
    """
    Handle booking of doctor appointments.

    This view handles the POST request for booking a doctor appointment. It creates and validates
    an AppointmentForm. If the form is valid and the user is not a doctor, it saves the appointment instance,
    and then redirects to the appointments page.

    If the request method is not POST, if the form is not valid, or if the user is a doctor,
    it renders the book_doctor_appointment.html template with the form.

    Parameters:
    request (HttpRequest): The HTTP request object.
    username (str): The username of the doctor.

    Returns:
    HttpResponse: The HTTP response. If the request method is POST, the form is valid, and the user is not a doctor,
                  it redirects to the appointments page. Otherwise, it renders the book_appointment.html template with
                  the form.
    """
    doctor = Doctor.objects.get(user__username=username)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        form.fields['timing'].queryset = Timing.objects.filter(doctor=doctor)
        if form.is_valid():
            # Check if the user is a doctor
            try:
                request.user.doctor
                error_message = "Doctors cannot book appointments for themselves."
                return render(request, 'book_doctor_appointment.html',
                              {'form': form, 'error_message': error_message, 'username': username})
            except Doctor.DoesNotExist:
                pass

            # Create a new Appointment instance
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.doctor = doctor
            appointment.date = timezone.now().date()
            appointment.save()
            return redirect('doctor_appointment_confirmation', username=username)
    else:
        form = AppointmentForm()
        form.fields['timing'].queryset = Timing.objects.filter(doctor=doctor)

    return render(request, 'book_doctor_appointment.html',
                  {'form': form, 'username': username})


def doctor_appointment_confirmation(request, username):
    """
    Display a confirmation message after an appointment is booked.

    This view renders the appointment_confirmation.html template, which displays a confirmation message.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response. It renders the appointment_confirmation.html template.
    """
    return render(request, 'doctor_appointment_confirmation.html')


def terms_conditions(request):
    """
   Render the Terms & Conditions page.

   This view renders the terms_conditions.html template.

   Parameters:
   request (HttpRequest): The HTTP request object.

   Returns:
   HttpResponse: The HTTP response that renders the terms_conditions.html template.
   """
    return render(request, 'terms_conditions.html')


def privacy_policy(request):
    """
   Render the Privacy Policy page.

   This view renders the privacy_policy.html template.

   Parameters:
   request (HttpRequest): The HTTP request object.

   Returns:
   HttpResponse: The HTTP response that renders the privacy_policy.html template.
   """
    return render(request, 'privacy_policy.html')


def about_us(request):
    """
   Render the About Us page.

   This view renders the about_us.html template.

   Parameters:
   request (HttpRequest): The HTTP request object.

   Returns:
   HttpResponse: The HTTP response that renders the about_us.html template.
   """
    return render(request, 'about_us.html')


def services(request):
    """
   Render the services page.

   This view renders the services.html template.

   Parameters:
   request (HttpRequest): The HTTP request object.

   Returns:
   HttpResponse: The HTTP response that renders the services.html template.
   """
    return render(request, 'services.html')


def emergency_services(request):
    """
   Render the emergency services page.

   This view renders the emergency_services.html template.

   Parameters:
   request (HttpRequest): The HTTP request object.

   Returns:
   HttpResponse: The HTTP response that renders the emergency_services.html template.
   """
    return render(request, 'emergency_services.html')


def doctors(request):
    """
  Render the doctors page.

  This view renders the doctors.html template.

  Parameters:
  request (HttpRequest): The HTTP request object.

  Returns:
  HttpResponse: The HTTP response that renders the doctors.html template.
  """
    return render(request, 'doctors.html')


def staff(request):
    """
  Render the staff page.

  This view renders the staff.html template.

  Parameters:
  request (HttpRequest): The HTTP request object.

  Returns:
  HttpResponse: The HTTP response that renders the staff.html template.
  """
    return render(request, 'staff.html')


def blood_bank(request):
    """
  Render the blood bank page.

  This view renders the blood_bank.html template.

  Parameters:
  request (HttpRequest): The HTTP request object.

  Returns:
  HttpResponse: The HTTP response that renders the blood_bank.html template.
  """
    return render(request, 'blood_bank.html')


def other_services(request):
    """
  Render the other services page.

  This view renders the other_services.html template.

  Parameters:
  request (HttpRequest): The HTTP request object.

  Returns:
  HttpResponse: The HTTP response that renders the other_services.html template.
  """
    return render(request, 'other_services.html')
