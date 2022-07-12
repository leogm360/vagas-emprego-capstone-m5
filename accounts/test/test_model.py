from django.test import TestCase

from accounts.models import Account


class AccountsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email= "a@a.com"
        cls.first_name = "a"
        cls.last_name = "b"
        cls.cpf = "12345678911"
        cls.gender = "Non-Binary"
        cls.phone = "99345678911"
        cls.is_human_resources = False