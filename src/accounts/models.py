from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models


class MyCustomManager(BaseUserManager):
    def create_user(self, email, password=None):
        """Creates and saves a User with the given email and password"""
        if not email:
            raise ValueError('Users must have an email addres.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        """Creates und saves a superuser with the given email and password"""
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save()
        return user


class MyCustomUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyCustomManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
