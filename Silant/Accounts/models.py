from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    role_description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.username