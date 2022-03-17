from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birth_date = models.DateTimeField(blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.URLField(blank=True)
    followers = models.ForeignKey(settings.INSTA_ACCOUNT, on_delete=models.CASCADE, related_name='followers_num', blank=True, null=True)
    following =  models.ForeignKey(settings.INSTA_ACCOUNT, on_delete=models.CASCADE, related_name='following_num', blank=True, null=True)
    def __str__(self):
        return f'{self.name} {self.surname}'
    def followers_num(self):
        return self.followers.count()
    def following_num(self):
        return self.following.count()