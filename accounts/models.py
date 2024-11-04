from django.db import models

# Create your models here
class Accounts(models.Model):
    cname=models.CharField(max_length=100)
    date=models.DateField()
