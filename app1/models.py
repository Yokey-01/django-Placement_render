from django.db import models

# Create your models here.
class Data1(models.Model):
    age = models.IntegerField()
    gender = models.IntegerField()
    stream = models.IntegerField()
    internships = models.IntegerField()
    cgpa = models.FloatField()
    hostel = models.IntegerField()
    historyofbacklog = models.IntegerField()
class signup(models.Model):
    username = models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)

