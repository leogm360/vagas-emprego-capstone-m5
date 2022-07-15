from django.test import TestCase

from addresses.models import Address

# Create your tests here.


class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.zip_code = "05010000"
        cls.street = "Av. Paulista"
        cls.number = 2000
        cls.city = "São Paulo"
        cls.state = "SP"
        cls.country = "Brasil"

        cls.address = Address.objects.create(
            zip_code=cls.zip_code,
            street=cls.street,
            number=cls.number,
            city=cls.city,
            state=cls.state,
            country=cls.country,
        )

    def test_zip_code_max_length(self):
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field("zip_code").max_length

        self.assertEquals(max_length, 8)

    def test_complement_can_be_null(self):
        address = Address.objects.get(id=1)

        self.assertIsNone(address.complement)

    def test_state_max_length(self):
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field("state").max_length

        self.assertEquals(max_length, 2)

    def test_address_has_information_fields(self):
        address = Address.objects.get(id=1)

        self.assertEqual(address.zip_code, self.zip_code)
        self.assertEqual(address.street, self.street)
        self.assertEqual(address.number, self.number)
        self.assertEqual(address.city, self.city)
        self.assertEqual(address.state, self.state)
        self.assertEqual(address.country, self.country)
