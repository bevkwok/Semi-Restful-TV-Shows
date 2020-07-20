from django.shortcuts import render, HttpResponse, redirect
from .models import Shows

def shows(request):
    context = {
        "all_shows" : Shows.objects.all() 
    }
    return render(request, 'shows.html', context)

def  new_show(request):
    form_title = request.GET['title']
    form_network = request.GET['network']
    form_release_date = request.GET['release_dat']
    create_show = Shows.objects.create(title=form_title, network =form_network, release_date=form_release_date)
    return redirect("/")
# Create your views here.
