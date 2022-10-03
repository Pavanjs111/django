from turtle import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    profile_url=models.URLField(blank=True)

    profile_img=models.ImageField(upload_to='profilepics',blank=True)