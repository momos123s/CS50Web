from django.contrib.auth import authenticate, login, logout,get_user_model
from django.db import IntegrityError
from django.db.models import F,Count
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
   
    data = User.objects.filter(username = userName )  
    data = data.values().first()
   
    #get follower and follwing counts
    following = Profile.objects.filter(user = userName)
    follower_count = following.count()
   

    #get the people user is following
    users_follows = following.get(user = userName)
    users_follows = users_follows.following.values().first()

    #get the users posts
    posts_collection = Post.objects.filter(userID = request.user.id).annotate(like_count=Count('likes__UserIDs')).order_by('timestamp')
    posts = []
    for post in posts_collection.values():
        print(post)
        posts.append({
        'id': post.get("postID"),
        'user': post.get("userID"),
        'description': post.get("description"),
        'likes': post.get("like_count"), 
        'views': post.get("views"),
        'timestamp': post.get("timestamp"),
    })

    
    following = following.values().first()
    data.update({ "users_posts":posts,"users_follows":users_follows,"followers_count":follower_count, "followers":following}) 
    return JsonResponse(data)

@login_required
def follow(request):
    return render(request,"network/follow.html")
    
@login_required
@csrf_exempt
def follow_view(request):

    
    
    if request.method == "GET":          
        follow_posts(request)
        return render(request, "network/follow.html")
    elif request.method == "PUT":
        #get the user to follows username
        data = json.loads(request.body)
        followersUsername= data.get("followid")
        
        #check if user has profile
        user2follow = User.objects.get(username = followersUsername) 
        profile = Profile.objects.get(user = request.user.id)

        #follow the request user if they are not followed
        if  not profile.following.filter( id = user2follow.pk).exists() and followersUsername != request.user.username :
            profile.following.add(user2follow)
            print("you are now following user")
            return JsonResponse({"status":"user was followed"})
        #unfollow requested user if followed 
        elif profile.following.filter(id = user2follow.pk).exists():
            profile.following.remove(user2follow)
            print("user was unfollowed")
            return JsonResponse({"status":"user has been unfollowed"})
        #error message incase something goes wrong
        else:
            return JsonResponse({"status":"you cannot follow yourself! or something else went worng"})
       
    else:
        return JsonResponse({"error":"An unknow error occured"})

@login_required
@csrf_exempt
def follow_posts(request,page_num):
    #find the users the user is following
    followersPosts = Profile.objects.get(user =request.user.id)
   
    posts_ = Post.objects 
    postCollection = None
    i = 1
    #use followers profiles to retreive their posts
    for post in followersPosts.following.values():
        #check if person followed has posts
        try:
            postCollection = (  (posts_.filter(userID = post.get('id'))))
        except:
           return render(request,"network/follow.html")
        i+=1
    try:
        postCollection = postCollection.annotate(like_count=Count('likes__UserIDs')).order_by('-timestamp')
    except:
        return render(request,"network/follow.html")
    
    print(postCollection.values())
    #paginate the posts 
    return posts(request,page_num,postCollection)
    

@login_required 
def get_posts(request,page_num):
    if request.method == "GET":
        post_data = Post.objects.annotate(like_count=Count('likes__UserIDs')).order_by('-timestamp')
        return posts(request,page_num,post_data)
    else:
        return JsonResponse({"error":"something went wrong"})

@login_required    
def posts(request, page_num,post_data):

        #get the likes and the posts
        
        print(post_data)
        # Paginate results
        paginator = Paginator(post_data, 10)
        posts_page = paginator.get_page(page_num)
        

        # Serialize posts and include the like_count
        posts = []
        for post in posts_page:
            
            posts.append({
                'id': post.postID,
                'user': post.userID.username,
                'description': post.description,
                'likes': post.like_count, 
                'views': post.views,
                'timestamp': post.timestamp,
            })
            
            
        response_data = {
            'posts': posts,
            'page': posts_page.number,
            'total_pages': paginator.num_pages,
            'has_next': posts_page.has_next(),
            'has_previous': posts_page.has_previous(),
            }
       

        return JsonResponse(response_data, safe=True)

#updates the likes
@csrf_exempt
@login_required
def update_likes(request):

    if request.method == 'PUT':

        #get front end data 
        data = json.loads(request.body)
        postid = data.get("id")
        userID =request.user

        #get data from database
        post = Likes.objects.get(postID = postid)
        isliked = Likes.objects.filter(postID = postid, UserIDs = userID).exists()
        print(isliked)

        #check if user has already liked the post
        if not isliked and request.user.is_authenticated:
            #like the post 
            post.UserIDs.add(userID)
            post.record = post.UserIDs.count()
            print(post.record)
            response = {"success":"post was liked", "amount":post.record,"isliked":isliked}
            return JsonResponse(response)
        
        #check if its liekd and remove like 
        elif isliked and request.user.is_authenticated:
            post.UserIDs.remove(userID)
            post.record = post.UserIDs.count()         
            print(post.record)
            response  = {"success":"post was unliked","amount":post.record,"isliked":isliked}
            return JsonResponse(response)
        else:
            return JsonResponse({"error":"something went wrong while trying to add like"})




@login_required
@csrf_exempt
def edit_description(request):
    if request.method == 'PUT':
        #retrieve description for user to edit
        data = json.loads(request.body)
        descrip = data.get("editContent")
        postid = data.get("id")
        description = Post.objects.get(postID = postid)
        #ensure user authentication and post is users 
        if request.user.is_authenticated and description.userID == request.user:
            description.description = descrip
            description.save()
            return JsonResponse({"response":" success"} )
        else:
            return JsonResponse({"error":"you cannot edit someone elses post"})
    else:
        return JsonResponse({"response": "something went wrong!"})

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
        profilePicture = request.POST["profilePicture"]                    

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
            profile = Profile()
            profile.user = user
            profile.profile_picture = profilePicture
            profile.save()


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
   
        #place items in database
        create_post = Post()
        create_post.userID = request.user
        print(request.user)
        create_post.username = request.user
        create_post.description = post_data[0]
        create_post.save()
        like = Likes()
        like.postID = create_post
        like.save()
 
        return HttpResponseRedirect(reverse("index"))
    else: 
        return JsonResponse({"error":"problem handling request"}, status = 300)
