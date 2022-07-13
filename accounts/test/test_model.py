import email

from accounts.models import Account
from django.test import TestCase


class AccountsModelTest(TestCase):
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
            password=cls.password,
            cpf=cls.cpf,
            gender=cls.gender,
            phone=cls.phone,
            is_human_resources=cls.is_human_resources,
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

    # Test Fields
    def test_fields_validated_email_name_cpf_phone(self):
        user = Account.objects.get(cpf=self.cpf)

        email_max_length = user._meta.get_field("email").max_length
        email_unique = user._meta.get_field("email").unique

        first_name_max_length = user._meta.get_field("first_name").max_length

        last_name_max_length = user._meta.get_field("last_name").max_length

        cpf_max_length = user._meta.get_field("cpf").max_length
        cpf_unique = user._meta.get_field("cpf").unique

        phone_max_length = user._meta.get_field("phone").max_length
        phone_unique = user._meta.get_field("phone").unique

        self.assertEquals(email_max_length, 255)
        self.assertEquals(email_unique, True)

        self.assertEquals(first_name_max_length, 50)
        self.assertEquals(last_name_max_length, 50)

        self.assertEquals(cpf_max_length, 11)
        self.assertEquals(cpf_unique, True)

        self.assertEquals(phone_max_length, 11)
        self.assertEquals(phone_unique, True)
