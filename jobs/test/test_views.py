from accounts.models import Account
from addresses.models import Address
from companies.models import Company
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from skills.models import Skill


class JobsViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print("\n\n Jobs Views Tests \n")

        cls.skill01 = Skill.objects.create(
            title="JS", description="Linguagem de programação."
        )
        cls.skill02 = Skill.objects.create(
            title="React", description="Framework."
        )

        cls.address01 = Address.objects.create(
            zip_code="0000000",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil",
        )

        cls.address2 = Address.objects.create(
            zip_code="0000001",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil",
        )

        cls.address3 = Address.objects.create(
            zip_code="0000002",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil",
        )

        cls.address4 = Address.objects.create(
            zip_code="0000003",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil",
        )

        cls.address5 = Address.objects.create(
            zip_code="0000005",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil",
        )

        cls.address6 = Address.objects.create(
            zip_code="0000006",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil",
        )

        cls.company01 = Company.objects.create(
            name="company1",
            cnpj="12345678912346",
            phone="12345678911",
            address=cls.address01,
        )

        cls.company02 = Company.objects.create(
            name="company2",
            cnpj="12345678912946",
            phone="12345678912",
            address=cls.address5,
        )

        cls.userCandidate01 = Account.objects.create(
            email="teste1@teste.com",
            password="1234",
            first_name="Teste",
            last_name="1",
            cpf="12345678911",
            gender="Cisgender",
            phone="91982010000",
            address=cls.address2,
        )

        cls.userCandidate02 = Account.objects.create(
            email="teste2@teste.com",
            password="1234",
            first_name="Teste",
            last_name="1",
            cpf="12345678921",
            gender="Cisgender",
            phone="91982050000",
            address=cls.address6,
        )

        cls.userRH01 = Account.objects.create(
            email="isRH@teste.com",
            password="1234",
            first_name="Teste",
            last_name="2",
            cpf="12345678913",
            gender="Cisgender",
            phone="91982020000",
            is_human_resources=True,
            company_id=cls.company01.id,
            address=cls.address3,
        )

        cls.userRH02 = Account.objects.create(
            email="isRH2@teste.com",
            password="1234",
            first_name="Teste",
            last_name="3",
            cpf="12345678914",
            gender="Cisgender",
            phone="91982040000",
            is_human_resources=True,
            company_id=cls.company02.id,
            address=cls.address4,
        )

        cls.superUser = Account.objects.create_superuser(
            email="admin@teste.com",
            password="1234",
            first_name="Teste",
            last_name="1",
            cpf="12345678912",
            gender="Cisgender",
            phone="91982000000",
        )

        cls.tokenUserRH01 = Token.objects.create(user=cls.userRH01)
        cls.tokenUserRH02 = Token.objects.create(user=cls.userRH02)
        cls.tokenUserCandidate01 = Token.objects.create(
            user=cls.userCandidate01
        )
        cls.tokenUserCandidate02 = Token.objects.create(
            user=cls.userCandidate02
        )

        cls.job01 = {
            "title": "Programador Front-End",
            "description": "Vaga para Desenvolvedor",
            "salary": 5000.00,
            "job_type": "CLT",
            "regimen_type": "HYBRID",
            "vacancies_count": 5,
            "skills_id": [cls.skill01.id, cls.skill02.id],
        }

    def test_create_job_only_authenticated_user_rh_sucess(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        res = self.client.post("/api/companies/jobs/register/", self.job01)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", res.data)
        self.assertIn("title", res.data)
        self.assertIn("description", res.data)
        self.assertIn("salary", res.data)
        self.assertIn("location", res.data)
        self.assertIn("job_type", res.data)
        self.assertIn("regimen_type", res.data)
        self.assertIn("vacancies_count", res.data)
        self.assertIn("subscribers_count", res.data)
        self.assertIn("issued_at", res.data)
        self.assertIn("company", res.data)
        self.assertEquals(res.data["company"]["name"], self.company01.name)
        self.assertEquals(res.data["company"]["cnpj"], self.company01.cnpj)
        self.assertEquals(res.data["company"]["phone"], self.company01.phone)

    def test_create_job_not_authenticated_fail(self):

        res = self.client.post("/api/companies/jobs/register/", self.job01)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", res.data)
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)

    def test_create_job_not_user_rh_fail(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserCandidate01.key
        )

        res = self.client.post("/api/companies/jobs/register/", self.job01)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("detail", res.data)
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)

    def test_create_job_missing_keys(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        res = self.client.post("/api/companies/jobs/register/", {})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", res.data)
        self.assertIn("description", res.data)
        self.assertIn("salary", res.data)
        self.assertIn("job_type", res.data)
        self.assertIn("regimen_type", res.data)
        self.assertIn("vacancies_count", res.data)

    def test_get_jobs(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        for _ in range(10):
            res = self.client.post("/api/companies/jobs/register/", self.job01)

        res_one = self.client.get("/api/companies/jobs/")

        self.assertEquals(res_one.status_code, status.HTTP_200_OK)
        self.assertEquals(res_one.data["count"], 10)
        self.assertTrue(res_one.data["next"])
        self.assertIsNone(res_one.data["previous"])

        next_page = res_one.data["next"]

        res_two = self.client.get(next_page)

        self.assertEquals(res_two.status_code, status.HTTP_200_OK)
        self.assertEquals(res_two.data["count"], 10)
        self.assertIsNone(res_two.data["next"])
        self.assertTrue(res_two.data["previous"])

        res_page_one = res_one.data["results"]
        res_page_two = res_two.data["results"]

        self.assertEquals(len(res_page_one + res_page_two), 10)

    def test_get_job_by_id(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        job = self.client.post("/api/companies/jobs/register/", self.job01)

        res = self.client.get("/api/companies/jobs/1/")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("id", res.data)
        self.assertIn("title", res.data)
        self.assertIn("description", res.data)
        self.assertIn("salary", res.data)
        self.assertIn("location", res.data)
        self.assertIn("job_type", res.data)
        self.assertIn("regimen_type", res.data)
        self.assertIn("vacancies_count", res.data)
        self.assertIn("subscribers_count", res.data)
        self.assertIn("issued_at", res.data)
        self.assertIn("company", res.data)
        self.assertEquals(res.data["company"]["name"], self.company01.name)
        self.assertEquals(res.data["company"]["cnpj"], self.company01.cnpj)
        self.assertEquals(res.data["company"]["phone"], self.company01.phone)

    def test_get_job_by_id_not_exist(self):
        res = self.client.get("/api/companies/jobs/555/")

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", res.data)
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)

    def test_patch_job_is_owner_company_rh_success(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        job = self.client.post("/api/companies/jobs/register/", self.job01)

        res = self.client.patch("/api/companies/jobs/1/", {"title": "Alterado"})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("id", res.data)
        self.assertIn("title", res.data)
        self.assertEquals(res.data["title"], "Alterado")
        self.assertIn("description", res.data)
        self.assertIn("salary", res.data)
        self.assertIn("location", res.data)
        self.assertIn("job_type", res.data)
        self.assertIn("regimen_type", res.data)
        self.assertIn("vacancies_count", res.data)
        self.assertIn("subscribers_count", res.data)
        self.assertIn("issued_at", res.data)
        self.assertIn("company", res.data)
        self.assertEquals(res.data["company"]["name"], self.company01.name)
        self.assertEquals(res.data["company"]["cnpj"], self.company01.cnpj)
        self.assertEquals(res.data["company"]["phone"], self.company01.phone)

    def test_patch_not_owner_company_rh_fail(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        job = self.client.post("/api/companies/jobs/register/", self.job01)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH02.key
        )

        res = self.client.patch(
            "/api/companies/jobs/1/", {"title": "Não Alterado"}
        )

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("detail", res.data)
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)

    def test_patch_job_by_id_not_exist(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        res = self.client.patch(
            "/api/companies/jobs/1/", {"title": "Não Alterado"}
        )

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", res.data)
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)

    def test_register_user_in_vacancie_job(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        job = self.client.post("/api/companies/jobs/register/", self.job01)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserCandidate01.key
        )

        res = self.client.patch("/api/accounts/jobs/1/")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("id", res.data)
        self.assertIn("title", res.data)
        self.assertIn("description", res.data)
        self.assertIn("salary", res.data)
        self.assertIn("location", res.data)
        self.assertIn("job_type", res.data)
        self.assertIn("regimen_type", res.data)
        self.assertIn("vacancies_count", res.data)
        self.assertIn("subscribers_count", res.data)
        self.assertEquals(res.data["subscribers_count"], 1)
        self.assertIn("issued_at", res.data)
        self.assertIn("company", res.data)
        self.assertEquals(res.data["company"]["name"], self.company01.name)
        self.assertEquals(res.data["company"]["cnpj"], self.company01.cnpj)
        self.assertEquals(res.data["company"]["phone"], self.company01.phone)

    def test_already_register_user_in_vacancie_job(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        job = self.client.post("/api/companies/jobs/register/", self.job01)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserCandidate01.key
        )

        register = self.client.patch("/api/accounts/jobs/1/")

        res = self.client.patch("/api/accounts/jobs/1/")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("job", res.data)
        self.assertEquals(
            res.data["job"],
            f"User {self.userCandidate01.first_name} {self.userCandidate01.last_name} cannot apply multiple times.",
        )
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)

    def test_register_not_user_in_vacancie_job_fail(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        job = self.client.post("/api/companies/jobs/register/", self.job01)

        res = self.client.patch("/api/accounts/jobs/1/")

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("detail", res.data)
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)

    def test_subscribers_count_in_register_job(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserRH01.key
        )

        job = self.client.post("/api/companies/jobs/register/", self.job01)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserCandidate01.key
        )

        register1 = self.client.patch("/api/accounts/jobs/1/")

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserCandidate02.key
        )

        res = self.client.patch("/api/accounts/jobs/1/")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("id", res.data)
        self.assertIn("title", res.data)
        self.assertIn("description", res.data)
        self.assertIn("salary", res.data)
        self.assertIn("location", res.data)
        self.assertIn("job_type", res.data)
        self.assertIn("regimen_type", res.data)
        self.assertIn("vacancies_count", res.data)
        self.assertIn("subscribers_count", res.data)
        self.assertEquals(res.data["subscribers_count"], 2)
        self.assertIn("issued_at", res.data)
        self.assertIn("company", res.data)
        self.assertEquals(res.data["company"]["name"], self.company01.name)
        self.assertEquals(res.data["company"]["cnpj"], self.company01.cnpj)
        self.assertEquals(res.data["company"]["phone"], self.company01.phone)

    def test_register_user_in_vacancie_job_not_found(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.tokenUserCandidate01.key
        )

        res = self.client.patch("/api/accounts/jobs/1/")

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", res.data)
        self.assertIn("status", res.data)
        self.assertIn("status_code", res.data)
