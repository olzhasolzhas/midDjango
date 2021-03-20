from django.db import models
from django.contrib.auth.models import User


class Man(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField('name')
    age = models.TextField('age')
    bd = models.DateField('birthday')


