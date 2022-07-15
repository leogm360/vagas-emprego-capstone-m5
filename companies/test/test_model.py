from django.db import IntegrityError
from django.test import TestCase
from ..models import Company
from django.utils import timezone
from addresses.models import Address
from addresses.serializers import AddressSerializer

# {
# "zip_code" :"sadasd,
# "street" :"asdasd",
# "number" :1,
# "complement" :"asd", 
# "city" :"asdas",
# "state" :"asdasd",
# country :"asdasd"
# }

class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        serializer = AddressSerializer(data={'zip_code': '2a', 'street': '112121', 'number': 1, 'complement': '12121', 'city': '1212', 'state': '11', 'country': '12121'})
        serializer.is_valid()

        cls.now = timezone.now()
        cls.name = "Test Company"
        cls.cnpj = "00000000000000"
        cls.phone = "00000000000"
        cls.date_joined = cls.now
        cls.address = Address.objects.create(**serializer.validated_data)

        cls.company = Company.objects.create(
            name=cls.name,
            cnpj=cls.cnpj, 
            phone=cls.phone,
            date_joined= cls.date_joined,
            address= cls.address,
        ) 

        


    # Testando atributos de comanpy.name
    def test_company_name(self):
        company = Company.objects.get(id=self.company.id)
        max_legnth  =  company._meta.get_field('name').max_length
        self.assertEquals(max_legnth,255)

    
    
    # Testando atributos de comanpy.cnpj
    def test_company_cnpj(self):
        company = Company.objects.get(id=self.company.id)

        max_legnth  =  company._meta.get_field('cnpj').max_length
        
        self.assertEquals(max_legnth,14) 



    # Testando atributos de comanpy.phone
    def test_company_phone(self):
        company = Company.objects.get(id=self.company.id)

        max_legnth  =  company._meta.get_field('phone').max_length

        self.assertEquals(max_legnth,11)    


    # Testando atributos de company.date_joined
    def test_company_date_joined(self):
        company = Company.objects.get(id=self.company.id)
        
        self.assertIsNotNone(company.date_joined)     


    # Testando atributos de company.adress_id
    def test_company_adress_id(self):
        company = Company.objects.get(id=self.company.id)

        self.assertTrue(company.address,Address)    

    def test_company_has_information_fields(self):              
        self.assertEqual(self.company.name, self.name)
        self.assertEqual(self.company.cnpj, self.cnpj)
        self.assertEqual(self.company.phone, self.phone)
        self.assertIsNotNone(self.company.date_joined)
        self.assertEqual(self.company.address, self.address)    