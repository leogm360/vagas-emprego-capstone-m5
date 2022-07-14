from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from accounts.models import Account

class EducationViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print('Executando Testes Views Educations')
        
        cls.userCandidate01 = Account.objects.create_user(email='teste1@teste.com', password="1234", first_name="Teste", last_name="1", cpf='12345678911',gender='Cisgender',phone='91982070039')
        cls.userNotCandidate01 = Account.objects.create_user(email='teste2@teste.com', password="1234", first_name="Teste", last_name="2", cpf='12345678912',gender='Cisgender',phone='91982070038', is_human_resources=True)

        cls.education01 = {'institution_name': 'Kenzie Academy', 'course':'FullStack Web','start_date':'2021-09-27',
        'end_date':'2022-09-27','certificate_link':'https://google.com.br/image'}

        # cls.education02 = {'institution_name': 'Kenzie Academy', 'course':'FullStack Web','start_date':'2021-09-27',
        # 'end_date':'2022-09-27','certificate_link':'https://google.com.br/image'}

        cls.tokenUser01 = Token.objects.create(user=cls.userCandidate01)
        cls.tokenUser02 = Token.objects.create(user=cls.userNotCandidate01)

    def test_create_education_only_authenticated_success(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        res = self.client.post('/api/accounts/education/', data=self.education01)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', res.data)
        self.assertIn('institution_name', res.data)
        self.assertIn('course', res.data)
        self.assertIn('start_date', res.data)
        self.assertIn('end_date', res.data)
        self.assertIn('certificate_link', res.data)
        self.assertIn('account_id', res.data)


    def test_create_education_not_authenticated_fail(self):
        res = self.client.post('/api/accounts/education/', data=self.education01)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)

        
        ...
    def test_create_education_not_candidate_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser02.key)
        res = self.client.post('/api/accounts/education/', data=self.education01)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('detail', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)


    def test_create_education_missing_keys(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        res = self.client.post('/api/accounts/education/', data={})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('institution_name', res.data)
        self.assertIn('course', res.data)
        self.assertIn('start_date', res.data)
        self.assertIn('end_date', res.data)
        self.assertIn('certificate_link', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)


    # def test_get_educations(self):
    #     self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)
    #     self.client.post('/api/accounts/education/', data=self.education01)
    #     self.client.post('/api/accounts/education/', data=self.education01)

    #     res = self.client.get('/api/accounts/education/')

    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertTrue(len(res.context['results']) == 2)
        
    def test_get_education_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        education = self.client.post('/api/accounts/education/', data=self.education01)

        res = self.client.get('/api/accounts/education/1/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('id', res.data)
        self.assertIn('institution_name', res.data)
        self.assertIn('course', res.data)
        self.assertIn('start_date', res.data)
        self.assertIn('end_date', res.data)
        self.assertIn('certificate_link', res.data)


    def test_get_education_by_id_not_exist(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        res = self.client.get('/api/accounts/education/555/')

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('detail', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)


    def test_patch_education_is_owner_success(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        education = self.client.post('/api/accounts/education/', data=self.education01)

        res = self.client.patch('/api/accounts/education/1/',data={'institution_name': 'Alterado'})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('id', res.data)
        self.assertIn('institution_name', res.data)
        self.assertIn('course', res.data)
        self.assertIn('start_date', res.data)
        self.assertIn('end_date', res.data)
        self.assertIn('certificate_link', res.data)
        
    def test_patch_education_not_is_owner_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        education = self.client.post('/api/accounts/education/', data=self.education01)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser02.key)

        res = self.client.patch('/api/accounts/education/1/',data={'institution_name': 'Não Alterado'})

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('You do not have permission to perform this action.', str(res.data['detail']))
        self.assertIn('detail', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)


    def test_patch_education_by_id_not_exist(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        res = self.client.patch('/api/accounts/education/555/')

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('detail', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)

    def test_delete_education_is_owner_success(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        education = self.client.post('/api/accounts/education/', data=self.education01)

        res = self.client.delete('/api/accounts/education/1/')

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_education_not_is_owner_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        education = self.client.post('/api/accounts/education/', data=self.education01)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser02.key)

        res = self.client.delete('/api/accounts/education/1/')

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('You do not have permission to perform this action.', str(res.data['detail']))
        self.assertIn('detail', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)

    def test_delete_education_by_id_not_exist(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser01.key)

        res = self.client.delete('/api/accounts/education/555/')

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('detail', res.data)
        self.assertIn('status', res.data)
        self.assertIn('status_code', res.data)