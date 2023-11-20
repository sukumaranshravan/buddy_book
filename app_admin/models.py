from django.db import models

# Create your models here.
class admin_tb(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)