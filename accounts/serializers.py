from addresses.serializers import AddressSerializer
from companies.serializers import CompanySerializer, CompanyUserSerializer
from educations.serializers import ListEducationSerializer
from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

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
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        user = Account.objects.create_user(**validated_data)

        return user


# Serializer para obrigar a passar a company id


class AccountSerializerIsRH(serializers.ModelSerializer):
    address = AddressSerializer()
    company_id = serializers.UUIDField(write_only=True)

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
        print(validated_data)

        return user


class ListAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


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
        read_only_fields = ["educations"]


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
