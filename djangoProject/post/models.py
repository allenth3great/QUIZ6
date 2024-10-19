from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, unique=True)

    USERNAME_FIELD = 'email'  # or 'username', depending on your preference
    REQUIRED_FIELDS = ['username', 'contact_number']

