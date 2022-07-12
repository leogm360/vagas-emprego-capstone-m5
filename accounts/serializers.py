from attr import fields
from rest_framework import serializers

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
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self, validated_data: dict):
        user = Account.objects.create_user(**validated_data)

        return user