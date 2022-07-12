from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError

from educations.models import Education

# Create your tests here.

class EducationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print('Executando o setUpData')

        # cls.user = User.objects.create_user=()
        cls.education = Education(institution_name='Kenzie Academy', course='FullStack Web',start_date='2021-09-27',end_date='2022-09-27',certificate_link='https://media-exp1.licdn.com/dms/image/C4E22AQHFYWuZij27pQ/feedshare-shrink_800/0/1645312473587?e=1659571200&v=beta&t=7eRbog9lRjfJHbtPD2L6LJGi1s3msB4UwuwHUZ_fq2A')

    def test_institution_name_max_length(self):
        institution = Education.objects.get(id=1)
        max_length = institution._meta.get_field('institution_name').max_length
        self.assertEquals(max_length, 255)

    def test_course_max_length(self):
        institution = Education.objects.get(id=1)
        max_length = institution._meta.get_field('course').max_length
        self.assertEquals(max_length, 20)
    
    def test_certificate_link_max_length(self):
        institution = Education.objects.get(id=1)
        max_length = institution._meta.get_field('certificate_link').max_length
        self.assertEquals(max_length, 255)

    def test_invalid_any_keys(self):
        with self.assertRaises(IntegrityError):
            newEducation = Education.objects.create(
                institution_name="first_name",
                course="last_name",
                start_date=None,
                end_date=None,
                certificate_link=True,
            )