# config/views.py
from django.shortcuts import render

def home (request):
    return render(request, "home.html")


def artists_list(request):
    return render(request, "artist/artists-list.html")

def editorial(request):
    return render(request, "editorial/editorial-index.html")

def events(request):
    return render(request, "events/events-index.html")
