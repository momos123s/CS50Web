from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass  

class Profile(models.Model):
    user = models.ForeignKey("User",on_delete=models.CASCADE,related_name="profile")
    following = models.ForeignKey("User", on_delete=models.CASCADE,related_name="follow" )


class Post(models.Model):
    userID = models.ForeignKey("User",on_delete=models.CASCADE)
    postID = models.BigAutoField(primary_key=True,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=99)
    description = models.TextField(null=False)
    mediaUpload = models.FileField(null=True, upload_to='media/')
    amountOfLikes = models.ForeignKey("Likes", on_delete=models.CASCADE,null=True)
    views = models.PositiveBigIntegerField(default=0)

class Likes(models.Model):
    record = models.PositiveBigIntegerField(default=0)
    postID = models.ForeignKey("Post",on_delete=models.CASCADE,null=True)
    UserIDs = models.ForeignKey("User", on_delete=models.CASCADE,null=True)

 