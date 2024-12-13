from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass  

class Profile(models.Model):
    ProfileID = models.BigAutoField(primary_key=True,unique=True)
    user = models.ForeignKey("User",on_delete=models.CASCADE,related_name="profile")
    following = models.ManyToManyField("User", related_name="follow" )


class Post(models.Model):
    userID = models.ForeignKey("User",on_delete=models.CASCADE)
    postID = models.BigAutoField(primary_key=True,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=False)
    mediaUpload = models.FileField(null=True, upload_to='media/')
    views = models.PositiveBigIntegerField(default=0)

class Likes(models.Model):
    id = models.BigAutoField(primary_key=True,unique=True)
    postID = models.ForeignKey("Post",on_delete=models.CASCADE,null=False)
    UserIDs = models.ManyToManyField("User", null=True)
    record = models.PositiveBigIntegerField(default=0)

 