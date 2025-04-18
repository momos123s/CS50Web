from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    cellPhone = models.CharField(null=False,max_length=120, verbose_name="cellphone number")
    location = models.GenericIPAddressField(protocol="both",unpack_ipv4=True, verbose_name="geolocation ip address")
    dateOfBirth = models.DateField(null=False, verbose_name="date of birth")
    Job = models.CharField(null=False, default="unemployed", max_length=256, verbose_name="Job Title" )
    EDUCATION_CHOICES = [
        ("highschool", "highschool"),
        ("bachelors", "bachelors"),
        ("masters", "masters"),
        ("phd", "phd"),
        ("other", "other"),
    ]
    education = models.CharField(null=False, choices=EDUCATION_CHOICES, max_length=256, verbose_name="education level")
    isValidated = models.BooleanField(default=False,null=False, verbose_name="cellphone validated")
    isSubscribed = models.BooleanField(default=False,null=False, verbose_name="user subscription")


class Psyche(models.Model):
    psycheID = models.BigAutoField(null=False, primary_key=True, unique=True)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)  
    PERSONALITY_TRAITS_CHOICES = [
        ("openness", "openness"),
        ("conscientiousness", "conscientiousness"),
        ("extraversion", "extraversion"),
        ("agreeableness", "agreeableness"),
        ("neuroticism", "neuroticism"),
    ]
    RELIGION_CHOICES = [
        ("christianity", "christianity"),
        ("islam", "islam"),
        ("hinduism", "hinduism"),
        ("buddhism", "buddhism"),
        ("judaism", "judaism"),
        ("atheism", "atheism"),
        ("agnosticism", "agnosticism"),
        ("other", "other"),
    ]
    personalityTraits = models.CharField(max_length=256, null=False, verbose_name="personality traits")
    religion = models.CharField(max_length=256, null=False, choices=RELIGION_CHOICES, verbose_name="religion")
    

class MediaFiles(models.Model):
    fileID = models.BigAutoField(primary_key=True, null=False, unique=True,verbose_name="Media Key")
    fileName = models.CharField(max_length=256, null=False, verbose_name="File name")
    fileData = models.FileField(upload_to="/media")
    fileDate = models.DateTimeField(auto_now=True, null=False, verbose_name="file upload date")
    uploader = models.ForeignKey( Person, on_delete=models.CASCADE, verbose_name="uploader")


class Messages(models.Model):
    MessageID = models.BigAutoField(primary_key=True, null=False, unique=True, verbose_name="message ID")
    message = models.TextField(null=False, verbose_name="Message")
    timestamp = models.DateTimeField(null=False, auto_now=True,verbose_name="time of message")
    sender = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="sender")
    reciever = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="reciever")
    file = models.ForeignKey(MediaFiles, on_delete=models.CASCADE, null=True, blank=True, verbose_name="file attached")

class Sexuality(models.Model):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    SexualityID = models.BigAutoField(primary_key=True, null=False, unique=True)
    SEX_CHOICES = [
        ("female", "female"),
        ("male", "male"),
        ("bigender", "bigender"),
    ]
    SEXUALITY_CHOICES = [
        ("straight", "straight"),
        ("bisexual", "bisexual"),
        ("lesbian","lesbian"),
        ("gay","gay"),
        ("pansexual","pansexual"),
        ("asexual","asexual"),
        ("queer","queer"),
        ("other","other"),
    ]
    sex = models.CharField(max_length=256, null=False,choices=SEX_CHOICES, verbose_name="sexual orientation")
    sexuality = models.CharField(max_length=256, null=False, choices=SEXUALITY_CHOICES, verbose_name="sexuality")

class Hobbies_Intreasts(models.Model):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    hobbiesID = models.BigAutoField(primary_key=True, null=False, unique=True)
    HOBBIES_CHOICES = [
        ("sports", "sports"),
        ("reading", "reading"),
        ("gaming", "gaming"),
        ("music", "music"),
        ("art", "art"),
        ("traveling", "traveling"),
        ("cooking", "cooking"),
        ("photography", "photography"),
        ("writing", "writing"),
        ("fitness", "fitness"),
        ("fashion", "fashion"),
        ("technology", "technology"),
        ("nature", "nature"),
        ("food", "food"),
    ]
    hobbies = models.CharField(max_length=256, null=False, choices=HOBBIES_CHOICES, verbose_name="hobbies")

class VisualAnalysis(models.Model):
    visualID = models.BigAutoField(primary_key=True, null=False, unique=True, verbose_name="visual ID")
    person = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name="persons looks")
    height = models.PositiveIntegerField(null=False ,verbose_name="persons height")
    weight = models.PositiveIntegerField(null=False, verbose_name="users weight")
    RACE_CHOICES = [
        ("white", "white"),
        ("black", "black"),
        ("asian", "asian"),
        ("hispanic", "hispanic"),
        ("mixed", "mixed"),
        ("other", "other"),
    ]
    BODY_TYPE_CHOICES = [
        ("skinny", "skinny"),
        ("fit", "fit"),
        ("average", "average"),
        ("chubby", "chubby"),
        ("Big", "Big"),
    ]
    race = models.CharField(null=False,choices=RACE_CHOICES, verbose_name="Race")
    bodyType = models.CharField(null=False, choices=BODY_TYPE_CHOICES, verbose_name="body type")

class PreferenceAnalysis(models.Model):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    PreferenceID = models.BigAutoField(primary_key=True, null=False, unique=True)



class Profile(models.Model):
    personID = models.ForeignKey( Person, on_delete=models.CASCADE,related_name="person")
    messageIDs = models.ManyToManyField( Messages)
    files = models.ManyToManyField(MediaFiles)
    visual = models.ForeignKey(VisualAnalysis, on_delete=models.CASCADE)
    Hobbies = models.ForeignKey(Hobbies_Intreasts, on_delete=models.CASCADE)
    preferences = models.ForeignKey(PreferenceAnalysis, on_delete=models.CASCADE)
    sexuality = models.ForeignKey(Sexuality, on_delete=models.CASCADE)
    psyche = models.ForeignKey(Psyche, on_delete=models.CASCADE)
