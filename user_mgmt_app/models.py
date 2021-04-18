from django.db import models

# Create your models here.

class Registered_users(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    