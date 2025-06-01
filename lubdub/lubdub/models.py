from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    cellPhone = models.CharField(null=False,max_length=120, verbose_name="cellphone number")
    location = models.CharField(max_length=100, blank=True, null=True)
    dateOfBirth = models.DateField(null=True, verbose_name="date of birth")
    Job = models.CharField(null=True, default="unemployed", max_length=256, verbose_name="Job Title" )
    EDUCATION_CHOICES = [
        ("highschool", "highschool"),
        ("bachelors", "bachelors"),
        ("masters", "masters"),
        ("phd", "phd"),
        ("other", "other"),
    ]
    education = models.CharField(null=True, choices=EDUCATION_CHOICES, max_length=256, verbose_name="education level")
    isValidated = models.BooleanField(default=False,null=True, verbose_name="cellphone validated")
    isSubscribed = models.BooleanField(default=False,null=True, verbose_name="user subscription")

 #   def __str__(self):
    #    return f"{self.username} - {self.cellPhone} - {self.location} - {self.dateOfBirth} - {self.Job} - {self.education} - {self.isValidated} - {self.isSubscribed}"



class Psyche(models.Model):
    psycheID = models.BigAutoField(null=False, primary_key=True, unique=True)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="human")  
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
    def __str__(self):
        return f"{self.personID.username} - {self.personalityTraits} ({self.religion})"



    

class MediaFiles(models.Model):
    fileID = models.BigAutoField(primary_key=True, null=False, unique=True,verbose_name="Media Key")
    fileName = models.CharField(max_length=256, null=False, verbose_name="File name")
    fileData = models.FileField(upload_to="media/")
    fileDate = models.DateTimeField(auto_now=True, null=False, verbose_name="file upload date")
    uploader = models.ForeignKey( Person, on_delete=models.CASCADE, verbose_name="uploader", related_name="uploader")
    
    def __str__(self):
        return f"{self.fileName} - {self.fileData} - {self.fileDate} - {self.uploader.username}"
class Match(models.Model):
    matchID = models.BigAutoField(primary_key=True, null=False, unique=True, verbose_name="match ID")
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person1")
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person2")
    matchDate = models.DateTimeField(auto_now=True, null=False, verbose_name="match date")
    isMatched = models.BooleanField(default=True)
    isBlocked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.person1.username} - {self.person2.username} - {self.matchDate} - {self.isMatched} - {self.isBlocked}"

class Messages(models.Model):
    MessageID = models.BigAutoField(primary_key=True, null=False, unique=True, verbose_name="message ID")
    matchID = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name="match ID", related_name="matched_couple")
    message = models.TextField(null=False, verbose_name="Message")
    timestamp = models.DateTimeField(null=False, auto_now=True,verbose_name="time of message")
    sender = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="sender")
    reciever = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="reciever")
    file = models.ForeignKey(MediaFiles, on_delete=models.CASCADE, null=True, blank=True, verbose_name="file attached")
    def __str__(self):
        return f"{self.matchID} - {self.message} - {self.timestamp} - {self.sender.username} - {self.reciever.username} - {self.file}"
class Sexuality(models.Model):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="humanSex")
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
    def __str__(self):
        return f"{self.personID.username} "
class Hobbies_Intreasts(models.Model):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="doer")
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

    def __str__(self):
        return f"{self.personID.username} - {self.hobbies} - {self.hobbiesID}"
class VisualAnalysis(models.Model):
    visualID = models.BigAutoField(primary_key=True, null=False, unique=True, verbose_name="visual ID")
    person = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name="personslooks" ,related_name="personsAppearance")
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
    race = models.CharField(max_length=80,null=False,choices=RACE_CHOICES, verbose_name="Race")
    bodyType = models.CharField(max_length=80,null=False, choices=BODY_TYPE_CHOICES, verbose_name="body type")
    def __str__(self):
        return f"{self.visualID} - {self.person.username} - {self.height} - {self.weight} - {self.race} - {self.bodyType} - {self.visualID}"
class PreferenceAnalysis(models.Model):
    personID = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="preferer")
    PreferenceID = models.BigAutoField(primary_key=True, null=False, unique=True)



class Profile(models.Model):
    personID = models.ForeignKey( Person, on_delete=models.CASCADE,related_name="profile")
    messageIDs = models.ManyToManyField( Messages)
    files = models.ManyToManyField(MediaFiles)
    visual = models.ForeignKey(VisualAnalysis, on_delete=models.CASCADE)
    Hobbies = models.ForeignKey(Hobbies_Intreasts, on_delete=models.CASCADE)
    preferences = models.ForeignKey(PreferenceAnalysis, on_delete=models.CASCADE)
    sexuality = models.ForeignKey(Sexuality, on_delete=models.CASCADE)
    psyche = models.ForeignKey(Psyche, on_delete=models.CASCADE)
    matches = models.ManyToManyField(Match)



#validate 
""" use pictures to check if user is:
real 
phone number validation is check 
email validation is checked 
age validation is checked
location is valid and vpn is not used 
user is subscribed to service and has paid the fee


if username is already taken return an error message 
if  cell phone number is already taken return an error message
if email is taken retuen error message 
if password is not strong enough return an error message
if date of birth is not valid return an error message
if not return an error message
"""

#prefernce analysis 
""" 

"""

#algorithm
#