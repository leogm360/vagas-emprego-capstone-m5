from attr import fields
from rest_framework import serializers

from educations.serializers import ListEducationSerializer

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
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
        ]
        read_only_fields = ["id", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        user = Account.objects.create_user(**validated_data)

        return user

class ListAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)


class AccountEducationsSerializer(serializers.ModelSerializer):
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
        read_only_fields = ['educations']


class ActiveDeactiveAccountSerializer(serializers.ModelSerializer):
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
            "is_active"
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