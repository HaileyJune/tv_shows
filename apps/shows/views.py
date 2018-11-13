from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import models
from .models import Shows
# from django.template import RequestContext
def index(request):
    context = {"shows" : Shows.objects.all()}
    return render (request, "shows/index.html", context)

def new(request):
    
    return render (request, "shows/new.html")

def create(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        Shows.objects.create(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release_date"], description = request.POST["description"])
    return redirect ("/shows")

def edit(request, num):
    context = {"show" : Shows.objects.get(id=num)}
    return render (request, "shows/edit.html", context)

def update(request, num):
    edit = Shows.objects.get(id = num)

    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/" + num + "/edit")
    # edit.objects.update(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release_date"], description = request.POST["description"])
    edit.title = request.POST["title"]
    edit.network = request.POST["network"]
    edit.release_date = request.POST["release_date"]
    edit.description = request.POST["description"]
    edit.save()
    return redirect("/shows/" +num)

def show(request, num):
    context = {"show" : Shows.objects.get(id = num)}
    return render (request, "shows/show.html", context)

def destroy(request, num):
    delete = Shows.objects.get(id=num)
    delete.delete()
    return redirect("/shows")