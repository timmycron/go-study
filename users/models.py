from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
"""
We use a custom user model with only email and password to prevent having to deal with a separate
username and to make it easier to add custom user fields in the future. 
"""


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Helper function to create a user with an email, password, and whatever extra info.
        See https://heemayl.net/posts/django-custom-user-model-without-username-field-and-using-email-in-place-of-it/
        :param email: str
        :param password: str
        :param extra_fields: dict
        :return: User
        """

        if not email:
            raise ValueError('User must have an email')

        if not password:
            raise ValueError('User must have a password')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Override create_user to ensure is_staff and is_superuser are default false
        :param email: str
        :param password: str
        :param extra_fields: dict
        :return: User
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Override create_superuser to ensure is_staff and is_superuser are true
        :param email: str
        :param password: str
        :param extra_fields: dict
        :return: User
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
