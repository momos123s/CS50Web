from django.contrib.auth import authenticate, login, logout,get_user_model
from django.db import IntegrityError
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.core.paginator import Paginator
import json
from .models import Post,User,Profile,Likes
from django.core import serializers


def index(request):
    #get all users data from data base and display 
        return render(request, "network/index.html")

@login_required
@csrf_exempt
def profile_view(request):
    #get users profile information 
    if request.method == "GET":   
        return render(request, "network/profile.html") 
  
    else:
        return JsonResponse({"error":"something went wrong"})

@login_required
@csrf_exempt
def load_profiles(request):
    userName = request.user
    print(userName)  
    data = User.objects.filter(username = userName )  
    data = data.values().first()
    followers = Profile.objects.filter(user = userName)
    following = Profile.objects.following
    follower_count = Profile.objects.count()
    data.update({"followers count":follower_count, "followers":followers})
    print(following)
    print(followers)
    print(follower_count)
    print(data) 
    return JsonResponse(data, safe=False)

    
@login_required
@csrf_exempt
def follow_view(request):
    
    if request.method == "GET":          
        follow_posts(request)
        return render(request, "network/follow.html")
    elif request.method == "PUT":
        #get the user to follows id
        data = json.loads(request.body)
        followersid = int(data.get("followid"))
        #put into data base
        user2Follow = Profile()
        user2Follow.user = request.user
        user2Follow.following = followersid
        user2Follow.save()
        return JsonResponse({"success":"following user"})
    else:
        return JsonResponse({"error":"An unknow error occured"})

@login_required
@csrf_exempt
def follow_posts(request):
    #find users follwers 
    followersPosts = Profile.objects.filter(user = request.user)
    print(followersPosts.values())
    posts = Post.objects 
    profileNums = len(followersPosts)
    postCollection = {}
    i = 0
    #use followers profiles to retreive their posts
    for post in followersPosts:
        if i == profileNums:
            break
        try:
            postCollection.update( {str(i): str((posts.filter(userID = post.user).values()[i]))})
        except:
            print("USER IS NOT FOLLOWING ANYONE!!")
        i+=1
    print(postCollection)
    return JsonResponse(postCollection, safe=False)
    

@login_required    
def get_posts(request, page_num):
    if request.method == 'GET': 
    
        post_data = Post.objects.all().order_by('timestamp')
        print(post_data.all().values())
        pag = Paginator(post_data, 10) 
        post = pag.get_page(page_num)
        print(Post.postID)
        #get profiles of each user who posts
        posts =serializers.serialize('json',post)
        response_data = {
            'posts': json.loads(posts),
            'page': post.number,
            'total_pages': pag.num_pages,
            'has_next': post.has_next(),
            'has_previous': post.has_previous(),
        }
        

        return JsonResponse(response_data, safe=True)
    else:
        return HttpResponse("<p>error<p>")

#updates the likes
@csrf_exempt
@login_required
def update_likes(request):

    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        liked = data.get("istrue")
        postid = data.get("id")
        userID =request.user
        #check if 
    return HttpResponse("")



@login_required
@csrf_exempt
def edit_description(request):
    if request.method == 'PUT':
        #retrieve description for user to edit
        data = json.loads(request.body)
        descrip = data.get("descript")
        description = Post.objects.get(User = request.user)
        description.description = descrip
        description.save()
        return JsonResponse({"response: success"})
    else:
        return JsonResponse({"response: something went wrong!"})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)    
            user.save()


        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

# create a new post
@csrf_protect
@login_required
def new_post(request):
    if request.method == "POST" and request.user.is_authenticated:
        #retrieve post data 
        data = json.loads(request.body)
        post_data = list(data.values())
        print(post_data[0])
        #place items in database
        create_post = Post()
        create_post.userID = request.user
        create_post.description = post_data[1]
        create_post.mediaUpload = post_data[0]
        create_post.save()
        create_post.save()
        like = Likes()
        like.postID = create_post
        like.UserIDs = None
        like.save()
        print(post_data)
        return JsonResponse({"success":"True"}, status =200 )
    else: 
        return JsonResponse({"error":"problem handling request"}, status = 300)
