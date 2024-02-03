from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, CreateListing, CreateListing_Form, Comments, CommentForm,Bids, BidsForm, Watchlist,Categories,CategoriesForm
from django.db.models import Max
from django.views.decorators.csrf import csrf_protect




@csrf_protect
@login_required
def categories(request):
    return render(request,"auctions/categories.html")

def index(request):
    listings = CreateListing.objects.all()
    return render(request, "auctions/index.html", {'listings': listings })

@csrf_protect
@login_required
def watchlist(request):   
    watch = Watchlist.objects.all()


    if request.method == "POST":
        userWatchlist = Watchlist()
        listingID = request.POST.get('listingID','')
        #check to see if user adds to watchlist
        if 'isOnWatchlist' in request.POST and User.is_authenticated:
            
            userWatchlist.userID = request.user
            userWatchlist.save()
            userWatchlist.itemId.set = listingID
            return HttpResponse("successfully added to list!") 
        else:
    # Check to see if user is deleting from watchlist
            n = Watchlist.objects.filter(itemId = listingID).delete()
            return HttpResponse("successfully deleted!")
        
    else:
        return render(request,"auctions/watchlist.html", {
            'watchlist':watch
        })
    

@login_required
@csrf_protect
def listing_page(request, pageNumber):
 
    #get the page
    listing = CreateListing.objects.filter(listingID = pageNumber)
    


    #form for bidding and comment section
    bidform = BidsForm()
    highestbid = Bids.objects.filter(listID = pageNumber).aggregate(Max("amountOfMoney"))
    highestbid = highestbid.get('amountOfMoney__max')
    comment = CommentForm()
    commentSection = Comments.objects.filter(listingID = pageNumber)
    onWatchlist = Watchlist.objects.filter(itemId = pageNumber, userID = request.user)
    try:
        print(onWatchlist[0])
    except:
        print("No")
    # check to see if page exists
    try: 
        listing[0]
    except:
        return HttpResponse("PAGE NOT FOUND!")
    
    user = CreateListing.objects.filter(listingID = pageNumber, creatorID = request.user.id)
    try:
         user[0]
         isUser = True
    except:
        isUser = False
  

    if listing[0].hasEnded == True:
        bid = Bids.objects.get(listID = pageNumber, amountOfMoney = highestbid )
        print(bid.bidderID)
        return render(request,"auctions/winner.html", {'info':listing[0], 'bid': bid})
    


    #post request for bidding and comment section
    elif request.method == "POST":
        #get post results
        comment = CommentForm(request.POST)
        bidform = BidsForm(request.POST)
        
        #validate forms 
        if bidform.is_valid() and User.is_authenticated and comment.errors:
            bidform.instance.bidderID = request.user
            bidform.instance.listID = CreateListing.objects.get(listingID=pageNumber)
            #save and refresh
            bidform.save()
            #update create list (poor data base design[many-to-many should have been used])
            createUpdate = CreateListing.objects.get(listingID = pageNumber)
            createUpdate.starting_bid = bidform.instance.amountOfMoney
            createUpdate.save()
            return HttpResponseRedirect(reverse("index"))
            #else:
                #return HttpResponse("your bid is too small to be place. bid must be greater then current bid")
        
        #validate forms
        elif comment.is_valid() and User.is_authenticated and bidform.errors :
            comment.instance.listingID = CreateListing.objects.get(listingID = pageNumber)
            comment.instance.commenterID = request.user
            comment.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            #display error if not valid
            return HttpResponse("something went wrong while trying to process your request")

    #display page elements 
    else:
        return render(request, "auctions/listingpage.html", {'pageInfo':listing[0], 
         'bidform':bidform, 'comment':comment, 'commentSection': commentSection, 'highestBid':highestbid, 'isUser':isUser})

@login_required
@csrf_protect
def deletelisting(request):
    #delete users page upon request
    if request.method == "POST":
        listingid = request.POST.get("listid","")
        #delete the page
        listing = CreateListing.objects.get( listingID = listingid)
        listing.hasEnded = True
        listing.save()
        print(listing.hasEnded)
        return HttpResponseRedirect(reverse("index"))

    return HttpResponse("Invalid request")


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    
    form = CreateListing_Form()
    newBid = Bids()
    categoryform = CategoriesForm()
    
    if request.method == "POST":
        # get post data form 
        form = CreateListing_Form(request.POST)
        #validate form
        if form.is_valid() and request.user.is_authenticated:
            form.instance.creatorID = request.user
            newBid = Bids()
           
            #save the users starting bid info
            form.instance.save()
            newBid.amountOfMoney = form.instance.starting_bid
            newBid.bidderID = request.user
            newBid.listID = form.instance
            newBid.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    
    else:
        return render(request,"auctions/createlisting.html", {'form':form, 'catergory':categoryform})

