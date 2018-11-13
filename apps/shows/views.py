from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from .models import Shows
# from django.template import RequestContext
def index(request):
    context = {"shows" : Shows.objects.all()}
    return render (request, "shows/index.html", context)

def new(request):
    # context = {"shows" : Shows.objects.all()}
    return render (request, "shows/new.html")

def create(request):
    Shows.objects.create(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release_date"], description = request.POST["description"])
    return redirect ("/shows")

def edit(request, num):
    context = {"show" : Shows.objects.get(id=num)}
    return render (request, "shows/edit.html", context)

def update(request, num):
    edit = Shows.objects.get(id = num)
    # edit.objects.update(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release_date"], description = request.POST["description"])
    edit.title = request.POST["title"]
    edit.network = request.POST["network"]
    edit.release_date = request.POST["release_date"]
    edit.description = request.POST["description"]
    edit.save()
    return redirect("/shows")

def show(request, num):
    context = {"show" : Shows.objects.get(id = num)}
    return render (request, "shows/show.html", context)

def destroy(request, num):
    delete = Shows.objects.get(id=num)
    delete.delete()
    return redirect("/shows")