from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.urls import reverse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Person, Psyche, MediaFiles, Match, Messages, Hobbies_Intreasts, VisualAnalysis, PreferenceAnalysis, Profile, Sexuality
# Create your views here.

#login view 
"""
user must fill the following fields:
    -username
    -password

check if user is regostered
if user is not registered, error message is displayed
if user is registered and username and password are correct, user is redirected to the main page
if username and password are not correct, desplay error message 
    """
def login_view(request):
    if request.method == "POST":
        login_info = json.loads(request.body)
        username = login_info.get("username")
        password = login_info.get("password")
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("MainView"))
    else:
        return JsonResponse({"failed":"auth attempt failed due to inavilidty"},status=400)

      #logout view
"""
user must be redirected to the login page 
"""
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_view"))




#regiser view 
"""
user must fill the following fields:
    - username
    - password
    - cell phone number
    - location
    - date of birth
    - job title
    - education level
    - personality traits
    - religion
    - profile pictures 
    
validation method must be called

if user is already registered, display error message & display the login page
if registration is successful, user is redirected to the main page
if user is not registered successfully, display error message 


"""
@csrf_protect
def register(request):
    if request.method == "GET":
        return render()
    
    elif request.method == "POST":
        reg_info = json.loads()
        return
    elif request.method=="PUT":
        return 
    else:
        return JsonResponse({"failed":"registration failed"}, status=400)




#Main view
"""
user must be logged in else redirect to login page

"""
@login_required
def MainView(request):
    return render("lubdub-react/lubdub-rjs/src/App.js")




#matching request view
""" 
if the user is not logged in, redirect to the login page

if the user is logged in, display the matching request page:
    -display the outgoing requests,
    -display the incoming requests,
    -display the matched users
    -display the unmatched users
    -display the blocked users

    if user accepts the request, display message and redirect them to the users mesasge page 
    if the user declines the request, display message of rejection 

"""

#profile view 
"""
if the user is not logged in, redirect to the login page
if the user is logged in, display the profile page (get request):
    -display the profile picture
    -display the username
    -display the cell phone number
    -display the location
    -display the date of birth
    -display the job title
    -display the education level
    -display the personality traits
    -display the religion
    -display the profile pictures 
    -display the hobbies and interests

to be used for swiping view as well
    

"""
#user profile view 
"""
if the user is logged in, display these elements of the profile:
    -username
    -cell phone number
    -location
    -date of birth
    -job title
    -education level
    -personality traits
    -religion
    -profile pictures 
    -swiping view 
    -message view


if the user is not logged in, redirect to the login page

"""
#Message view 
"""
if the user is logged in, has selected profile to message and view:
    display the messages between the two users
    display the files sent and recieved 

    if the user sends a message use a POST request to send the message
      store the message in the database 
      display the message in the message view  to confrim the message was sent 

    else display error or warning message 

"""

#swiping view

