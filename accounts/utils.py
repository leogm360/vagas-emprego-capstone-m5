from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_superuser, is_human_resources, **extra_fields
    ):
        now = timezone.now()

        if not email:
            print(email)
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_superuser=is_superuser,
            is_human_resources=is_human_resources,
            is_active=True,
            date_joined=now,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, is_human_resources, **extra_fields):
        return self._create_user(
            email, password, False, is_human_resources, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, False, **extra_fields)
