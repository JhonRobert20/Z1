from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):

    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email", unique=True, null=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username']