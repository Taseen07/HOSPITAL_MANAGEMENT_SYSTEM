# Import required modules
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Doctor, Patient, Appointment, Timing


class DoctorModelTest(TestCase):
    """
    Test case for the Doctor model.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.doctor = Doctor.objects.create(
            user=self.user,
            description='Test doctor',
            department='Test department',
            phone_number='1234567890',
            nid='12345678901234567890',
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_doctor_creation(self):
        """
        Test doctor creation.
        """
        self.assertTrue(isinstance(self.doctor, Doctor))
        self.assertEqual(self.doctor.__str__(), self.doctor.user.username)


class PatientModelTest(TestCase):
    """
    Test case for the Patient model.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.patient = Patient.objects.create(
            user=self.user,
            age=30,
            blood_group='A+',
            phone_number='1234567890',
            nid='12345678901234567890',
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_patient_creation(self):
        """
        Test patient creation.
        """
        self.assertTrue(isinstance(self.patient, Patient))
        self.assertEqual(self.patient.__str__(), self.patient.user.username)


class RegisterDoctorViewTest(TestCase):
    """
    Test case for the register_doctor view.
    """

    def setUp(self):
        """
        Set up test client.
        """
        self.client = Client()

    def test_register_doctor_view(self):
        """
        Test register_doctor view.
        """
        response = self.client.get(reverse('register_doctor'))

        # Check status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_doctor.html')


class RegisterPatientViewTest(TestCase):
    """
    Test case for the register_patient view.
    """

    def setUp(self):
        """
        Set up test client.
        """
        self.client = Client()

    def test_register_patient_view(self):
        """
        Test register_patient view.
        """

        # Test GET request
        response = self.client.get(reverse('register_patient'))

        # Check status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_patient.html')


class SearchViewTest(TestCase):
    """
    Test case for the search view.
    """

    def setUp(self):
        """
        Set up test data and client.
        """

        # Create two doctors
        self.user1 = User.objects.create_user(username='doctor1', first_name='John', last_name='Doe')
        self.doctor1 = Doctor.objects.create(
            user=self.user1,
            description='Test doctor 1',
            department='Test department',
            phone_number='1234567890',
            nid='12345678901234567890',
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

        self.user2 = User.objects.create_user(username='doctor2', first_name='Jane', last_name='Doe')
        self.doctor2 = Doctor.objects.create(
            user=self.user2,
            description='Test doctor 2',
            department='Test department',
            phone_number='1234567890',
            nid='12345678901234567890',
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_search_view(self):
        """Test search view"""

        # Test GET request
        response = self.client.get(reverse('search'))

        # Check status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage/homepage.html")

        # Test POST request with no doctors found
        response = self.client.post(reverse('search'), {'search_term': 'Nonexistent'})

        # Check if error message is displayed
        self.assertContains(response, 'No doctor found')

        # Test POST request with one doctor found by first name
        response = self.client.post(reverse('search'), {'search_term': 'John'})

        # Check if correct doctor is found
        self.assertContains(response, 'John Doe')

        # Test POST request with one doctor found by last name
        response = self.client.post(reverse('search'), {'search_term': 'Doe'})

        # Check if correct doctors are found
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'Jane Doe')

        # Test POST request with multiple doctors found by full name
        response = self.client.post(reverse('search'), {'search_term': 'John Doe'})

        # Check if correct doctor is found
        self.assertContains(response, 'John Doe')


class AppointmentBookingTest(TestCase):
    """
    Test case for the book_doctor_appointment view.
    """

    def setUp(self):
        """
        Set up test data and client.
        """

        # Create a doctor and a patient
        self.user1 = User.objects.create_user(username='doctor1', first_name='John', last_name='Doe')
        self.doctor = Doctor.objects.create(
            user=self.user1,
            description='Test doctor',
            department='Test department',
            phone_number='1234567890',
            nid='12345678901234567890',
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

        self.user2 = User.objects.create_user(username='patient1', first_name='Jane', last_name='Doe')
        self.patient = Patient.objects.create(
            user=self.user2,
            age=30,
            blood_group='A+',
            phone_number='1234567890',
            nid='12345678901234567890',
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_book_doctor_appointment_view(self):
        """
        Test book_doctor_appointment view.
        """

        # Log in as patient
        self.client.login(username='patient2', password='patientpatient')

        # Test GET request
        response = self.client.get(reverse('book_doctor_appointment', args=[self.doctor.user.username]))

        # Check status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_doctor_appointment.html')

        # Test POST request with valid data
        response = self.client.post(reverse('book_doctor_appointment', args=[self.doctor.user.username]), {
            'timing': 1
        })

        # Check if appointment is created and redirected to confirmation page
        # self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('doctor_appointment_confirmation', args=[self.doctor.user.username]))
        # self.assertEqual(Appointment.objects.count(), 1)
