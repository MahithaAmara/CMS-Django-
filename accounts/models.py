from django.db import models

# Create your models here
class accounts(models.Model):
    cname=models.CharField(max_length=100)
    date=models.DateField()
    pno=models.IntegerField()
