from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Shows

def shows(request):
    context = {
        "all_shows" : Shows.objects.all() 
    }
    return render(request, 'shows.html', context)

def  new_show(request):
    context = {
        "all_shows" : Shows.objects.all() 
    }
    return render(request, 'new_show.html', context)

def create_show(request):
    form_title = request.POST['title']
    form_network = request.POST['network']
    form_release_date = request.POST['release_date']
    create_show = Shows.objects.create(title=form_title, network =form_network, release_date=form_release_date)
    return redirect("/shows/news")

def edit_show(request, show_id):
    context = {
        "all_shows" : Shows.objects.all(), 
        "show" : Shows.objects.get(id=show_id),
    }
    return render(request, 'edit_show.html', context)

def update_show(request):
    form_show_id = request.POST['hidden_show_id']
    show = Shows.objects.get(id=form_show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.save()
    return redirect("shows/" + form_show_id + "/edit")

def display_show(request, show_id):
    context = {
        "all_shows" : Shows.objects.all(), 
        "show" : Shows.objects.get(id=show_id),
    }
    return render(request, 'display_show.html', context)
# Create your views here.
