from django.test import TestCase
from skills.models import Skill


class SkillModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print("\n\n Skills Model Tests \n")

        cls.skill_one = {
            "title": "HTML5",
            "description": """
              HTML5 é uma linguagem de marcação para a World Wide Web e é uma
              tecnologia chave da Internet, originalmente proposto por Opera
              Software. É a quinta versão da linguagem HTML.
            """,
        }

        cls.created_skill_one = Skill.objects.create(**cls.skill_one)

    def test_model_skill_title_field(self):
        skill: Skill = Skill.objects.get(pk=self.created_skill_one.id)

        title_max_length = skill._meta.get_field("title").max_length
        title_unique = skill._meta.get_field("title").unique

        self.assertEqual(title_max_length, 50)
        self.assertTrue(title_unique)
        self.assertEquals(skill.title, self.skill_one["title"])

    def test_model_skill_description_field(self):
        skill: Skill = Skill.objects.get(pk=self.created_skill_one.id)

        self.assertEquals(skill.description, self.skill_one["description"])

    def test_model_skill_ordering_meta_data(self):
        skill: Skill = Skill.objects.get(pk=self.created_skill_one.id)

        self.assertEqual(skill._meta.ordering[0], "id")

    def test_model_skill_representation(self):
        skill: Skill = Skill.objects.get(pk=self.created_skill_one.id)

        skill_repr = f"<Skill: title - {self.skill_one['title']}>"

        self.assertEquals(repr(skill), skill_repr)
