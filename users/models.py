from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    A custom user model to allow for future expansion.
    """
    email = models.EmailField(unique=True)

    # Required for Django's authentication system
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
