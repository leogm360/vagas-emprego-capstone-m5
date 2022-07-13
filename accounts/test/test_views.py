from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account

class TestAccountsViews(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email= "a@a.com"
        cls.first_name = "a"
        cls.last_name = "b"
        cls.password= "1234"
        cls.cpf = "12345678911"
        cls.gender = "Non-Binary"
        cls.phone = "99345678911"
        cls.is_human_resources = False

        cls.admin = Account.objects.create_superuser(
            email=cls.email,
            first_name=cls.first_name,
            last_name=cls.last_name,
            password=cls.password,
            cpf=cls.cpf,
            gender=cls.gender,
            phone=cls.phone,
            is_human_resources=cls.is_human_resources
        )

        cls.recruiter = Account.objects.create_user(
            email="recruiter@hr.com",
            first_name="Recrutino",
            last_name="Smallboss",
            password=cls.password,
            cpf="11122233311",
            gender=cls.gender,
            phone="99911122233",
            is_human_resources=True
        )

        cls.candidate = Account.objects.create_user(
            email="candidate@jr.com",
            first_name="Candito",
            last_name="Jobs",
            password=cls.password,
            cpf="13125234311",
            gender=cls.gender,
            phone="99814122533",
            is_human_resources=False
        )

        cls.token_adm = Token.objects.create(user=cls.admin)

        cls.token_candidate = Token.objects.create(user=cls.candidate)

        cls.token_recruiter = Token.objects.create(user=cls.recruiter)

        cls.candidate_data = {
            "email":"candidate2@jr.com",
            "first_name":"Candito",
            "last_name":"Jobs",
            "password":cls.password,
            "cpf":"13121234311",
            "gender":cls.gender,
            "phone":"99814112333",
            "is_human_resources":False
        }

        cls.recruiter_data = {
            "email":"recruiter2@hr.com",
            "first_name":"Recrutino",
            "last_name":"Smallboss",
            "password":cls.password,
            "cpf":"11122232111",
            "gender":cls.gender,
            "phone":"99911321233",
            "is_human_resources":True
        }
