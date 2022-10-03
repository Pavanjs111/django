from django.db import models

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    price=models.IntegerField()
    p_date=models.DateField()

