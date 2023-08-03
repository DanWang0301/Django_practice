from django.db import models

# Create your models here.
class User(models.Model):
    User_Name = models.TextField(max_length=100, )
    User_Email = models.TextField(max_length=100, )
    User_Password = models.TextField(max_length=100, )
    User_Authorized = models.ForeignKey('Authorized', related_name='User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_come_date = models.DateTimeField(auto_now=True)

class Authorized(models.Model):
    Authorized = models.TextField()
