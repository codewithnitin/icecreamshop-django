from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.models import Post
from datetime import datetime
from django.contrib import messages

import requests
import json

# Create your views here.

def index(request):
    context = {
        "variable1" : "This is sent",
        "Variable2" : "That is sent"
    }
    return(render(request, "index.html", context))
    # return(HttpResponse("This is homepage"))


def about(request):
    return (render(request, "about.html"))
    # return(HttpResponse("This is about page"))

def services(request):
    return (render(request, "services.html"))
    # return(HttpResponse("This is service page"))

def services1(request):
    return (render(request, "services1.html"))

def services2(request):
    return (render(request, "services2.html"))

def offer(request):
    return (render(request, "offer.html"))


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name= name, email= email, phone= phone, desc= desc, date= datetime.today())
        contact.save()

        messages.success(request, "Your message has been sent!")


    return (render(request, "contact.html"))
    # return(HttpResponse("This is contact page"))

def search(request):
    if request.method == "POST":
        query = request.POST.get("query")
        allposts = Post.objects.filter(title__icontains= query)
        params = {"allposts" : allposts, "query" : query}
        return(render(request, "search.html", params))







