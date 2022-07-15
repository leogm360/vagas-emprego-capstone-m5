from datetime import timezone
from rest_framework.test import APITestCase
from accounts.models import Account
from addresses.models import Address
from companies.models import Company
import datetime





class CompaniesViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.now = datetime.datetime.now()
        cls.address = Address.objects.create(
            zip_code="0000000",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil"
            )
        
        cls.address2 = Address.objects.create(
            zip_code="0000000",
            street="Test",
            number=123,
            complement="House",
            city="São Paulo",
            state="SP",
            country="Brazil"
            )
        

        cls.company = Company.objects.create(
           name="company2",
            cnpj="12345678912346", 
            phone="12345678911",
            date_joined=cls.now,
            address= cls.address,
        ) 
        cls.company2 = Company.objects.create(
            name="company2",
            cnpj="12345678912345", 
            phone="12345678911",
            date_joined= cls.now,
            address= cls.address2,
        ) 


        cls.admin = Account.objects.create_superuser(
            email="a@a.com",
            first_name= "a",
            last_name="b",
            password="1234",
            cpf="12345678911",
            gender="Non-Binary",
            phone="99345678911",
        )

        cls.recruiter = Account.objects.create_user(
            email="recruiter@hr.com",
            first_name="Recrutino",
            last_name="Smallboss",
            password="1234",
            cpf="11122233311",
            gender="Non-Binary",
            phone="99911122233",
            is_human_resources=True,
        )

        cls.candidate = Account.objects.create_user(
            email="candidate@jr.com",
            first_name="Candito",
            last_name="Jobs",
            password="1234",
            cpf="13125234311",
            gender="Non-Binary",
            phone="99814122533",
            is_human_resources=False,
        )

    def test_can_list_all_companies(self):    
        response = self.client.get('/api/companies/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data),4) 

    def test_can_list_one_company(self):  
        response = self.client.get(f'/api/companies/{self.company2.id}/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data),6)     

    def test_cannot_register_company_without_keys(self):
        self.client.force_authenticate(user=self.admin)
        post_response = self.client.post('/api/companies/',{}, format='json')

        self.assertEqual(post_response.status_code, 400)

        self.assertEquals(post_response.data,{
                    "address": [
                        "This field is required."
                    ],
                    "name": [
                        "This field is required."
                    ],
                    "cnpj": [
                        "This field is required."
                    ],
                    "phone": [
                        "This field is required."
                    ],
                    "status": "error",
                    "status_code": 400
        })    

    
    def test_candidate_cannot_register_company_(self):
        self.client.force_authenticate(user=self.candidate)
        post_response = self.client.post('/api/companies/',{
            "name": "company test",
	        "cnpj": "888888",
	        "phone":"88888",
	        "address": {
                "zip_code":81815,
                "street" :"asdasd",
                "number" :1,
                "complement" :"asd", 
                "city" :"asdas",
                "state" :"as",
                "country" :"asdasd"
                }
        }, format='json')


        self.assertEqual(post_response.status_code, 403)

        self.assertEquals(post_response.data,{
                "detail": "You do not have permission to perform this action.",
                "status": "error",
                "status_code": 403
            })

    def test_recruiter_cannot_register_company_(self):
        self.client.force_authenticate(user=self.recruiter)
        post_response = self.client.post('/api/companies/',{
            "name": "company test",
	        "cnpj": "888888",
	        "phone":"88888",
	        "address": {
                "zip_code":81815,
                "street" :"asdasd",
                "number" :1,
                "complement" :"asd", 
                "city" :"asdas",
                "state" :"as",
                "country" :"asdasd"
                }
        }, format='json')


        self.assertEqual(post_response.status_code, 403)
        self.assertEquals(post_response.data,{
                "detail": "You do not have permission to perform this action.",
                "status": "error",
                "status_code": 403
            })

    def test_admin_can_register_company_(self):
        self.client.force_authenticate(user=self.admin)
        post_response = self.client.post('/api/companies/',{
            "name": "company test",
	        "cnpj": "888888",
	        "phone":"88888",
	        "address": {
                "zip_code":81815,
                "street" :"asdasd",
                "number" :1,
                "complement" :"asd", 
                "city" :"asdas",
                "state" :"as",
                "country" :"asdasd"
                }
        }, format='json')


        self.assertEqual(post_response.status_code, 201)

    def test_admin_can_update_a_company_(self):
        self.client.force_authenticate(user=self.admin)
        patch_response = self.client.patch(f'/api/companies/{self.company2.id}/',{
            "name": "update test"}, format='json')
        
        self.assertEqual(patch_response.status_code, 200)

    def test_admin_can_delete_a_company_(self):
        self.client.force_authenticate(user=self.admin)
        patch_response = self.client.delete(f'/api/companies/{self.company2.id}/')
        
        self.assertEqual(patch_response.status_code, 204)    


