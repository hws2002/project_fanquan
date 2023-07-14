from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class User(AbstractUser):
#     # Add additional fields as per your requirements
#     bio = models.TextField(blank=True)

#     # Add any other custom fields here
#     def __str__(self):
#         return self.username

class Group(models.Model):
    group_name = models.CharField(max_length=200,default="",unique=True)
    group_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # def _is_manager_this(manager)
    
    def __str__(self):
        return self.group_name