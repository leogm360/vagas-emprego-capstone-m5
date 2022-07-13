from django.db import IntegrityError
from django.test import TestCase
from ..models import Company
from django.utils import timezone
import re

class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.now = timezone.now()
        cls.name = "Test Company"
        cls.cnpj = "00.000.000/0001-00"
        cls.phone = "00000-0000"
        cls.date_joined = cls.now
        cls.adress_id = 1

        cls.company = Company.objects.create(
            name=cls.name,
            cnpj=cls.cnpj, 
            phone=cls.phone,
            date_joined= cls.date_joined,
            adress_id= cls.adress_id,
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

        regex = r'[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}'

        self.assertTrue(re.fullmatch(regex, company.cnpj))
        self.assertEquals(max_legnth,14) 



    # Testando atributos de comanpy.phone
    def test_company_phone(self):
        company = Company.objects.get(id=self.company.id)

        max_legnth  =  company._meta.get_field('phone').max_length

        self.assertEquals(max_legnth,11)    


    # Testando atributos de company.date_joined
    def test_company_date_joined(self):
        company = Company.objects.get(id=self.company.id)
        
        self.assertEquals(company.date_joined,self.company.date_joined)     


    # Testando atributos de company.adress_id
    def test_company_adress_id(self):
        company = Company.objects.get(id=self.company.id)

        self.assertTrue(int(company.adress_id))    

    def test_company_has_information_fields(self):              
        self.assertEqual(self.company.name, self.name)
        self.assertEqual(self.company.cnpj, self.cnpj)
        self.assertEqual(self.company.phone, self.phone)
        self.assertEqual(self.company.date_joined, self.date_joined)
        self.assertEqual(self.company.adress_id, self.adress_id)    