from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import util
import markdown2
import random
from django.views.decorators.csrf import csrf_protect


def index(request):
    #get a list of all the wiki pages that exist 
    return render(request , "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):

    #creates edit page to edit the wiki page
    edit_page_url = reverse('edit_page', kwargs={'entry': title})
    edit_page_link = f"<a href='{edit_page_url}'>Edit Page</a>"
    #error here, supposed to grab last part of url
    title = util.get_entry(title)

    # check if site exists 
    if title != None:

        #convert markdown string to html and save it 
        filePath = "encyclopedia/search.html"
        wiki_html = markdown2.markdown(title)
        wiki_html += edit_page_link
        
        #open file and write html contents 
        with open("/home/molemo/Documents/CS50W/wiki/encyclopedia/templates/encyclopedia/search.html" ,'w') as f:
            f.write(wiki_html)

        # send user to requested site
        return render(request, filePath, {'wiki_html': wiki_html})
       
    #return error message if the site doesnt exist
    else:
        return HttpResponse("PAGE DOES NOT EXIST")

@csrf_protect
def search(request):

    if request.method == "POST":
        #get the user input
        searchQuery = request.POST.get('q', None)
        #take user input and validate it
        if searchQuery is not None:
            return redirect(reverse('wiki', args=[searchQuery]))
        else:
            return HttpResponse("PLEASE TYPE IN A PAGE")


@csrf_protect
def new_page(request):

    if request.method == 'POST':
     #get users page entry 
        content = request.POST.get('content', None)
        page_title = request.POST.get('page_title', None)
        page_checker = util.get_entry(request.POST.get('page_title', None))
        print(page_title)
        #check if new page already exists and validate data
        if page_checker is not None or page_title is None or content is None:
            return HttpResponse("PAGE ALREADY EXISTS")
        else:
            #convert from a string to markdown
            util.save_entry(page_title,content)
            page_loader = "wiki/" + page_title
            print(page_loader)
            return redirect(page_loader)
    else:
        return render(request, "encyclopedia/new_wiki.html")

@csrf_protect
def edit_page (request, entry):
    if request.method == "POST":
        #get post data
        content = request.POST.get('CONTENT', None)
        title = request.POST.get('PAGETITLE', None)
        #validate data and store
        if content is not None or title is not None:
            util.save_entry(title,content)
            return redirect(reverse('wiki', args=[title]))
        else:
            return HttpResponse("please ensure the page has content ")

    else:
        pageInMD = util.get_entry(entry)
        title = entry
        print(pageInMD)
        return render(request, "encyclopedia/edit_page.html", {
            "content": pageInMD,
            "page_title": title
        })



def random_wiki(request):
    #get entries 
    entries = util.list_entries()
    #select random page
    randomNum = random.randint(0,len(entries)-1)
    random_page = entries[randomNum]
    #go to random page
    return redirect(reverse('wiki', args=[random_page])) 