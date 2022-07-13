from django.test import TestCase
from django.utils import timezone
from accounts.models import Account
from jobs.models import Job

# Create your tests here.
class JobTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.userCandidate = Account.objects.create_user(email='teste@teste.com', password="1234", first_name="Teste", last_name="Teste", cpf='12345678910', gender='Cisgender', phone='989898989',is_human_resources=False)
        cls.now = timezone.now()

        cls.title = "desenvolvedor"
        cls.description = "Test model job"
        cls.salary = 3000.00
        cls.location =  "Curitiba-PR"
        cls.job_type = "CLT"
        cls.regimen_type = "REMOTE"
        cls.vacancies_count = 3
        cls.subscribers_count = 15
        cls.issued_at = cls.now
        cls.is_active = True
        cls.account = cls.userCandidate

    def test_job_title_max_length(self):
        job = Job.objects.get(id=1)
        max_length = job._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_job_location_max_length(self):
        job = Job.objects.get(id=1)
        max_length = job._meta.get_field('location').max_length
        self.assertEquals(max_length, 50)

    def test_job_job_type_max_length(self):
        job = Job.objects.get(id=1)
        max_length = job._meta.get_field('job_type').max_length
        self.assertEquals(max_length, 9)        

    def test_job_regimen_type_max_length(self):
        job = Job.objects.get(id=1)
        max_length = job._meta.get_field('regimen_type').max_length
        self.assertEquals(max_length, 10)