from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from educations.models import Education

class EducationViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.userCandidate01 = {'email':'teste1@teste.com','password': '1234','first_name':'Candidato', 'last_name':'01','cpf': '12345678912', 'gender':'Masculino','phone':'91982070039'}

        cls.education01 = {'institution_name': 'Kenzie Academy', 'course':'FullStack Web','start_date':'2021-09-27',
        'end_date':'2022-09-27','certificate_link':'https://media-exp1.licdn.com/dms/image/C4E22AQHFYWuZij27pQ/feedshare-shrink_800/0/1645312473587?e=1659571200&v=beta&t=7eRbog9lRjfJHbtPD2L6LJGi1s3msB4UwuwHUZ_fq2A'}

        # cls.education02 = {'institution_name': 'Kenzie Academy', 'course':'FullStack Web','start_date':'2021-09-27',
        # 'end_date':'2022-09-27','certificate_link':'https://media-exp1.licdn.com/dms/image/C4E22AQHFYWuZij27pQ/feedshare-shrink_800/0/1645312473587?e=1659571200&v=beta&t=7eRbog9lRjfJHbtPD2L6LJGi1s3msB4UwuwHUZ_fq2A'}

    def test_create_education_only_authenticated_success(self):
        ...
    def test_create_education_not_authenticated_fail(self):
        ...
    def test_create_education_not_candidate_fail(self):
        ...
    def test_create_education_missing_keys(self):
        ...
    def test_get_educations(self):
        ...
    def test_get_education_by_id(self):
        ...
    def test_get_education_by_id_not_exist(self):
        ...
    def test_patch_education_is_owner_success(self):
        ...
    def test_patch_education_not_is_owner_fail(self):
        ...