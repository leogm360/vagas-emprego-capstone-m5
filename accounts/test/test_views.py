from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account

import ipdb
 # ipdb.set_trace()
class TestAccountsViews(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "a@a.com"
        cls.first_name = "a"
        cls.last_name = "b"
        cls.password = "1234"
        cls.cpf = "12345678911"
        cls.gender = "Non-Binary"
        cls.phone = "99345678911"
        cls.is_human_resources = False

        cls.admin = Account.objects.create_superuser(
            email=cls.email,
            first_name=cls.first_name,
            last_name=cls.last_name,
            cpf=cls.cpf,
            gender=cls.gender,
            phone=cls.phone,
            password=cls.password
        )

        cls.recruiter = Account.objects.create_user(
            email="recruiter@hr.com",
            first_name="Recrutino",
            last_name="Smallboss",
            password=cls.password,
            cpf="11122233311",
            gender=cls.gender,
            phone="99911122233",
            is_human_resources=True,
        )

        cls.candidate = Account.objects.create_user(
            email="candidate@jr.com",
            first_name="Candito",
            last_name="Jobs",
            password=cls.password,
            cpf="13125234311",
            gender=cls.gender,
            phone="99814122533",
            is_human_resources=False,
        )

        cls.token_adm = Token.objects.create(user=cls.admin)

        cls.token_candidate = Token.objects.create(user=cls.candidate)

        cls.token_recruiter = Token.objects.create(user=cls.recruiter)

        cls.candidate_data = {
            "email": "candidate2@jr.com",
            "password": "1234",
            "first_name": "Candito",
            "last_name": "Jobs",
            "cpf": "13121234311",
            "gender": "Cisgender",
            "phone": "99814112333",
            "is_human_resources": "false"
        }

        cls.recruiter_data = {
            "email": "recruiter2@hr.com",
            "password": "1234",
            "first_name": "Recrutino",
            "last_name": "Smallboss",
            "cpf": "11122232111",
            "gender": "Cisgender",
            "phone": "99911321233",
            "is_human_resources": "true"
        }

    def test_register_account_candidate(self):
        res = self.client.post("/api/accounts/register/", data=self.candidate_data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_register_account_recruiter(self):
        res = self.client.post("/api/accounts/register/", data=self.recruiter_data)
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
        self.client.post("/api/accounts/register/", data=self.recruiter_data)
        res = self.client.post("/api/accounts/register/", data=self.recruiter_data)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("email", res.data)
        self.assertIn("already exists", str(res.data["email"]))

        self.assertIn("cpf", res.data)
        self.assertIn("already exists", str(res.data["cpf"]))

        self.assertIn("phone", res.data)
        self.assertIn("already exists", str(res.data["phone"]))


    

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
            "email":"candidate@jr.com",
            "password":"1234"
        }
        res = self.client.post("/api/accounts/login/", data=login_data )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.candidate.auth_token.key, res.data["token"])    


    def test_login_account_recruiter_sucess(self):
        login_data = {
            "email":"recruiter@hr.com",
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

