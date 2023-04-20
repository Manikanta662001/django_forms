from django.db import models

# Create your models here.
class Name(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    courses=models.CharField(max_length=100)
