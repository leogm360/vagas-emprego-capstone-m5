from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account

import ipdb
from addresses.models import Address
from companies.models import Company

from skills.models import Skill
 # ipdb.set_trace()
class TestAccountsViews(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.skill01 = Skill.objects.create(title="JS", description="Linguagem de programação.")
        cls.skill02 = Skill.objects.create(title="React", description="Framework.")

        cls.address01 = Address.objects.create(
            zip_code="0000000",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil"
            )

        cls.address2 = Address.objects.create(
            zip_code="0000001",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil"
            )

        cls.address3 = Address.objects.create(
            zip_code="0000002",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil"
            )

        cls.address4 = Address.objects.create(
            zip_code="0000003",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil"
            )
        

        # cls.address3 = {
        #         "zip_code":"0000002",
        #         "street":"Test",
        #         "number":"123",
        #         "complement":"House",
        #         "city":"São Paulo",
        #         "state":"SP",
        #         "country":"Brazil"
        #     }

        # cls.address4 = {
        #         "zip_code":"0000003",
        #         "street":"Test",
        #         "number":"123",
        #         "complement":"House",
        #         "city":"São Paulo",
        #         "state":"SP",
        #         "country":"Brazil"
        #     }


        cls.company01 = Company.objects.create(
            name="company1",
            cnpj="12345678912346", 
            phone="12345678911",
            address= cls.address01,
            )

        cls.admin = Account.objects.create_superuser(
            email="a@a.com",
            first_name="a",
            last_name="b",
            cpf="12345678911",
            gender="Non-Binary",
            phone="99345678911",
            password="1234"
        )

        cls.recruiter = Account.objects.create_user(
            email="recruiter@hr.com",
            first_name="Recrutino",
            last_name="Smallboss",
            password="1234",
            cpf="11122233311",
            gender="Non-Binary",
            phone="99911122233",
            is_human_resources=True
        )


        cls.candidate = Account.objects.create(
            email="candidate@jr.com",
            first_name="Candito",
            last_name="Jobs",
            password="1234",
            cpf="13125234311",
            gender="Non-Binary",
            phone="99814122533",
            address=cls.address2
        )

        cls.candidate.skills.set([cls.skill01.id,cls.skill02.id])

        cls.token_adm = Token.objects.create(user=cls.admin)

        cls.token_candidate = Token.objects.create(user=cls.candidate)

        cls.token_recruiter = Token.objects.create(user=cls.recruiter)


        cls.candidate01 = {
            "email": "candidate2@teste.com",
            "password": "1234",
            "first_name": "Candito",
            "last_name": "Jobs",
            "cpf": "88888888888",
            "gender": "Male",
            "phone": "99814112322",
            "address": cls.address3,
            "skills_id": [cls.skill01.id,cls.skill02.id]
        }

        cls.recruiter01 = {
            "email": "recruiter2@teste.com",
            "password": "1234",
            "first_name": "Recrutino",
            "last_name": "Smallboss",
            "cpf": "99999999999",
            "gender": "Male",
            "phone": "99911321233",
            "address": cls.address4,
            "is_human_resources": "true",
            "company_id": cls.company01.id
        }

    def test_register_account_candidate(self):
        res = self.client.post("/api/accounts/register/", data=self.candidate01)
        # ipdb.set_trace()


        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_register_account_recruiter(self):
        res = self.client.post("/api/accounts/register/", data=self.recruiter01)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_register_missing_keys(self):
        res = self.client.post("/api/accounts/register/", data={})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", res.data)
        self.assertIn("password", res.data)
        self.assertIn("first_name", res.data)
        self.assertIn("last_name", res.data)
        self.assertIn("cpf", res.data)
        self.assertIn("gender", res.data)
        self.assertIn("phone", res.data)

    def test_register_email_cpf_phone_already_existy(self):
        self.client.post("/api/accounts/register/", data=self.recruiter01)
        res = self.client.post("/api/accounts/register/", data=self.recruiter01)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    

    def test_only_adm_can_list_accounts(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_adm.key)

        res = self.client.get("/api/accounts/")

        # ipdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_login_account_adm_sucess(self):
        login_data = {
            "email":"a@a.com",
            "password":"1234"
        }
        res = self.client.post("/api/accounts/login/", data=login_data )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.admin.auth_token.key, res.data["token"])    

    
    def test_login_account_candidate_sucess(self):
        login_data = {
            "email":"candidate@teste.com",
            "password":"1234"
        }
        res = self.client.post("/api/accounts/login/", data=login_data )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.candidate.auth_token.key, res.data["token"])    


    def test_login_account_recruiter_sucess(self):
        login_data = {
            "email":"recruiter@teste.com",
            "password":"1234"
        }
        res = self.client.post("/api/accounts/login/", data=login_data )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.recruiter.auth_token.key, res.data["token"])    



    def test_only_owner_account_can_list_your_account(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_candidate.key)

        res = self.client.get(f"/api/accounts/{self.candidate.id}/")

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_only_owner_account_can_update_your_account(self):
        updated_data = {
            "first_name":"Atualizado",
            "last_name":"Atualizado"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_candidate.key)

        res = self.client.patch(f"/api/accounts/{self.candidate.id}/", data=updated_data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_only_owner_account_can_delete_your_account(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_candidate.key)

        res = self.client.delete(f"/api/accounts/{self.candidate.id}/")

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


    def test_only_owner_account_can_list_jobs_registred(self):
        ...


    def test_only_recruiter_can_add_company(self):
        ...


    def test_reactive_account(self):
        ...


    def test_only_adm_can_active_deactive_account(self):
        activate = {
            "is_active": True
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_adm.key)

        res = self.client.patch(
            f'/api/accounts/{self.admin.id}/management/activation/', data=activate
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

