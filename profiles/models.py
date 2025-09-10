from django.db import models
from users.models import User

class Profile(models.Model):
    """
    User profile model to store personal details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    interests = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
