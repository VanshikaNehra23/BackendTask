from django.db import models
from django.contrib.auth.models import AbstractUser

class Events(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    capacity = models.IntegerField()
    availability = models.IntegerField()
    opentime = models.TimeField()
    closetime = models.TimeField()

    def __str__(self):
        return self.name

class Waiting(models.Model):
    event_name = models.ForeignKey(Events,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

class UserRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ForeignKey(Events)


    def __str__(self):
        return self.user

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=1)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


