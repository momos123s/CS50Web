from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.forms import ModelForm
from django import forms

class User(AbstractUser):
    pass

class CreateListing(models.Model):
    
    creatorID = models.ForeignKey("User", on_delete = models.CASCADE)
    listingID = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 30)
    description = models.TextField(null = True)
    starting_bid = models.PositiveBigIntegerField(null = True)
    picture = models.URLField(null = True)
    startdate = models.DateTimeField(auto_now_add=True)
    hasEnded = models.BooleanField(default = False)

class CreateListing_Form(ModelForm):
    class Meta:
        model = CreateListing
        fields = ["title", "description", "starting_bid", "picture"]
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.URLInput(attrs={'class': 'form-control', 'placeholder':'url for picture'}),}


class Bids(models.Model):
    bidderID = models.ForeignKey("User", on_delete=models.CASCADE)
    listID = models.ForeignKey( "createListing",on_delete=models.CASCADE)
    biddID = models.BigAutoField(primary_key=True)
    amountOfMoney = models.BigIntegerField(null = True)
    dateOfBid = models.DateTimeField(auto_now_add=True)

class BidsForm(ModelForm):
    class Meta:
        model = Bids
        fields = ["amountOfMoney"]
        widgets = {
            'amountOfMoney':forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Comments(models.Model):
    listingID = models.ForeignKey("CreateListing",on_delete=models.CASCADE)
    commentID = models.AutoField(primary_key=True)
    commenterID = models.ForeignKey("User",on_delete=models.CASCADE)
    comment = models.TextField(null =True)
    dateOfComment = models.DateTimeField(auto_now_add=True)

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["comment"]
        widgets = {
            'comment': forms.Textarea(attrs= {'class': 'form-control'})
        }

class Watchlist(models.Model):
    itemId = models.ManyToManyField("CreateListing")
    userID = models.ForeignKey("User", on_delete=models.CASCADE)

class Categories(models.Model):
    listingIDs = models.ManyToManyField("CreateListing")
    categoryID = models.AutoField( primary_key=True)
    name = models.CharField(max_length=50)

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["name"]  