from addresses.serializers import AddressSerializer
from django.core.exceptions import ObjectDoesNotExist
from educations.serializers import ListEducationSerializer
from rest_framework.serializers import (
    CharField,
    EmailField,
    IntegerField,
    ListField,
    ModelSerializer,
    Serializer,
    UUIDField,
    ValidationError,
)
from skills.models import Skill

from .models import Account


class AccountSerializer(ModelSerializer):
    address = AddressSerializer()
    skills_id = ListField(
        child=IntegerField(min_value=0),
        allow_empty=False,
        write_only=True,
    )

    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "cpf",
            "gender",
            "phone",
            "address",
            "skills_id",
            "skills",
            "is_human_resources",
        ]
        depth = 1

        extra_kwargs = {"password": {"write_only": True}}

    def set_skills(self, user: Account, skills_data: dict) -> None:
        errors = {}

        for skill_id in skills_data:
            try:
                skill = Skill.objects.get(pk=skill_id)

                user.skills.add(skill)
            except ObjectDoesNotExist:
                if not errors.get("skills", False):
                    errors["skills"] = []

                errors["skills"].append(
                    f"Skill with id {skill_id} does not exist."
                )

        if errors.get("skills", False):
            raise ValidationError(errors)

    def create(self, validated_data: dict):
        skills_data = validated_data.pop("skills_id")

        user = Account.objects.create_user(**validated_data)

        self.set_skills(user, skills_data)

        return user

    def update(self, instance, validated_data: dict) -> Account:
        skills_data = validated_data.pop("skills_id", False)

        user = super().update(instance, validated_data)

        if skills_data:
            self.set_skills(user, skills_data)

        user.save()

        return user


class AccountSerializerIsRH(ModelSerializer):
    address = AddressSerializer()
    company_id = UUIDField(write_only=True)

    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "cpf",
            "gender",
            "phone",
            "address",
            "is_human_resources",
            "is_superuser",
            "company",
            "company_id",
        ]
        read_only_fields = ["is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        user = Account.objects.create_user(**validated_data)

        return user


class ListAccountsSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializer(Serializer):
    email = EmailField(max_length=255)
    password = CharField(write_only=True)


class AccountEducationsSerializer(ModelSerializer):
    educations = ListEducationSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = [
            "email",
            "first_name",
            "last_name",
            "cpf",
            "educations",
        ]
        read_only_fields = ["educations"]


class ActiveDeactiveAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "cpf",
            "gender",
            "phone",
            "is_human_resources",
            "is_superuser",
            "is_active",
        ]
        read_only_fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "cpf",
            "gender",
            "phone",
            "is_human_resources",
            "is_superuser",
        ]
