from django.test import TestCase
from django.core.exceptions import ValidationError
from accounts.models import Account
from addresses.models import Address
from companies.models import Company
from jobs.models import Job

# Create your tests here.
class JobTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.address01 = Address.objects.create(
            zip_code="0000000",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil"
        )

        cls.company01 = Company.objects.create(
            name="company1",
            cnpj="12345678912346", 
            phone="12345678911",
            address= cls.address01,
            )

        cls.userCandidate = Account.objects.create_user(
            email='teste@teste.com',
            password="1234",
            first_name="Teste",
            last_name="Teste",
            cpf='12345678910',
            gender='Cisgender',
            phone='989898989',
        )

        cls.job = Job.objects.create(title='Programador',description='Vaga para Desenvolvedor',salary=5000.00,location='Curitiba',job_type= 'CLT',regimen_type= 'HYBRID',vacancies_count= 5, company=cls.company01)
        cls.job_wrong = Job(title='Programador',description='Vaga para Desenvolvedor',salary=5000.00,location='Curitiba',job_type= 'CLT',regimen_type= 'HYBRID',vacancies_count= -10, company=cls.company01)

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

    def test_quantity_vacancies_min_value(self):
        with self.assertRaises(ValidationError):
            if self.job_wrong.full_clean():
                self.job_wrong.save()