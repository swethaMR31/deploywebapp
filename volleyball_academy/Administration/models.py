from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

'''class Candidate(models.Model):
    CHOICES = [('1', 'Male'),
               ('2', 'Female')]
    name=models.CharField(max_length=20)
    #dob=models.DateField(max_length=10)
    #gender=models.IntegerField(choices=CHOICES)
    session=models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    #Address = models.CharField(max_length=20)
    #phone_no = models.IntegerField(max_length=10)
    #declaration=models.BooleanField(max_length=20)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name'''
CHOICES = [('Male', 'Male'),
           ('Female', 'Female')]
option = [('Beginner', 'Beginner'),
           ('Intermediate', 'Intermediate'),('Advanced', 'Advanced')]

from django.db import models
class Player(models.Model):
    name = models.CharField("name", max_length=255, blank = True, null = True)
    dob=models.DateField(max_length=10,null = True)
    gender=models.CharField(choices=CHOICES, null = True, max_length=25)
    standard=models.CharField(choices=option,null = True, max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    #DOJ = models.DateTimeField("doj", auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField("name", max_length=255)
    dob=models.DateField(max_length=10,null = True)
    gender=models.CharField(choices=CHOICES, null = True, max_length=25)
    experience=models.IntegerField()
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20, null = True)
    address = models.TextField(blank=True, null=True)
    DOJ = models.DateTimeField("doj", auto_now_add=True)

    def __str__(self):
        return self.name