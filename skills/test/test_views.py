from accounts.models import Account
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from rest_framework.test import APITestCase
from skills.models import Skill
from skills.serializers import SkillSerializer


class SkillViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.skill_data = {
            "title": "HTML5",
            "description": "HTML5 é uma linguagem de marcação para a World Wide Web e é uma tecnologia chave da Internet, originalmente proposto por Opera Software. É a quinta versão da linguagem HTML.",
        }

        cls.skills_list = [
            Skill.objects.create(
                **{
                    "title": f"Skill Title {count}",
                    "description": f"Skill description {count}.",
                }
            )
            for count in range(10)
        ]

        cls.response_not_found = {
            "detail": "Not found.",
            "status": "error",
            "status_code": HTTP_404_NOT_FOUND,
        }

        cls.response_filter_required = {
            "q": ["This field is required."],
            "status": "error",
            "status_code": HTTP_400_BAD_REQUEST,
        }

        superuser = Account.objects.create_superuser(
            **{
                "email": "admin@email.com",
                "first_name": "Admin",
                "last_name": "User",
                "gender": "Cisgender",
                "password": "134679@#Adm",
            }
        )

        token, _ = Token.objects.get_or_create(user=superuser)

        cls.token = token.key

    def setUp(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_view_skill_create_success(self):
        res = self.client.post("/api/skills/", self.skill_data, format="json")

        self.assertEquals(res.status_code, HTTP_201_CREATED)
        self.assertDictContainsSubset(self.skill_data, res.data)

    def test_view_skill_create_missing_data_400_fail(self):
        res = self.client.post("/api/skills/", {}, format="json")

        response_example = {
            "title": ["This field is required."],
            "description": ["This field is required."],
            "status": "error",
            "status_code": HTTP_400_BAD_REQUEST,
        }

        self.assertEquals(res.status_code, HTTP_400_BAD_REQUEST)
        self.assertEquals(response_example, res.data)

    def test_view_skill_list_success(self):
        skills_count = 10

        res_one = self.client.get("/api/skills/")

        self.assertEquals(res_one.status_code, HTTP_200_OK)
        self.assertEquals(res_one.data["count"], skills_count)
        self.assertTrue(res_one.data["next"])
        self.assertIsNone(res_one.data["previous"])

        next_page = res_one.data["next"]

        res_two = self.client.get(next_page)

        self.assertEquals(res_two.status_code, HTTP_200_OK)
        self.assertEquals(res_two.data["count"], skills_count)
        self.assertIsNone(res_two.data["next"])
        self.assertTrue(res_two.data["previous"])

        res_page_one = res_one.data["results"]
        res_page_two = res_two.data["results"]

        self.assertEquals(
            len(res_page_one + res_page_two), len(self.skills_list)
        )

        for skill in self.skills_list:
            serialized_skill_data = SkillSerializer(instance=skill).data

            self.assertIn(serialized_skill_data, res_page_one + res_page_two)

    def test_view_skill_retrieve_success(self):
        created_skill = self.client.post(
            "/api/skills/", self.skill_data, format="json"
        )

        res = self.client.get(f"/api/skills/{created_skill.data['id']}/")

        self.assertEquals(res.status_code, HTTP_200_OK)
        self.assertDictContainsSubset(self.skill_data, res.data)

    def test_view_skill_retrieve_invalid_id_404_fail(self):
        invalid_id = 9999999

        res = self.client.get(f"/api/skills/{invalid_id}/")

        self.assertEquals(res.status_code, HTTP_404_NOT_FOUND)
        self.assertEquals(self.response_not_found, res.data)

    def test_view_skill_update_success(self):
        created_skill = self.client.post(
            "/api/skills/", self.skill_data, format="json"
        )

        data_to_update = {
            "title": "CSS3",
            "description": "CSS3 é a terceira mais nova versão das famosas Cascading Style Sheets, pela qual se define estilos para um projeto web. Com efeitos de transição, imagem, imagem de fundo/background e outros, pode-se criar estilos únicos para seus projetos web, alterando diversos aspectos de design no layout da página.",
        }

        res = self.client.patch(
            f"/api/skills/{created_skill.data['id']}/",
            data_to_update,
            format="json",
        )

        self.assertEquals(res.status_code, HTTP_200_OK)
        self.assertDictContainsSubset(data_to_update, res.data)

    def test_view_skill_update_invalid_id_404_fail(self):
        invalid_id = 9999999

        res = self.client.patch(f"/api/skills/{invalid_id}/")

        self.assertEquals(res.status_code, HTTP_404_NOT_FOUND)
        self.assertEquals(self.response_not_found, res.data)

    def test_view_skill_delete_success(self):
        created_skill = self.client.post(
            "/api/skills/", self.skill_data, format="json"
        )

        res = self.client.delete(f"/api/skills/{created_skill.data['id']}/")

        self.assertEquals(res.status_code, HTTP_204_NO_CONTENT)
        self.assertIsNone(res.data)

    def test_view_skill_delete_invalid_id_404_fail(self):
        invalid_id = 9999999

        res = self.client.delete(f"/api/skills/{invalid_id}/")

        self.assertEquals(res.status_code, HTTP_404_NOT_FOUND)
        self.assertEquals(self.response_not_found, res.data)

    def test_view_skill_search_skill_success(self):
        skills_count = 1

        self.client.post("/api/skills/", self.skill_data, format="json")

        res = self.client.get(
            f"/api/skills/search/?q={self.skill_data['title']}"
        )

        self.assertEquals(res.status_code, HTTP_200_OK)
        self.assertEquals(res.data["count"], skills_count)
        self.assertIsNone(res.data["next"])
        self.assertIsNone(res.data["previous"])
        self.assertDictContainsSubset(self.skill_data, res.data["results"][0])

    def test_view_skill_search_skill_400_fail(self):
        res = self.client.get(f"/api/skills/search/")

        self.assertEquals(res.status_code, HTTP_400_BAD_REQUEST)
        self.assertEquals(self.response_filter_required, res.data)
