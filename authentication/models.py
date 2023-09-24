from django.db import models

# Create your models here.

class Registration(models.Model):
    username = models.TextField(max_length=30)
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)