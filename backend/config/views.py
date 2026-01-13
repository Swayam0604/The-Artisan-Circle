# config/views.py
from django.shortcuts import render
from apps.accounts.models import ArtistProfile
from apps.artworks.models import Artwork

def home (request):
    return render(request, "home.html")

def artwork_list(request):
    artworks = (
        Artwork.objects
        .filter(is_for_sale=True)
        .select_related("artist")
        .prefetch_related("images")
        .order_by("-created_at")
    )

    return render(
        request,
        "artworks/artworks-list.html",
        {"artworks": artworks}
    )
    

def artists_list(request):
    artists = ArtistProfile.objects.all().order_by("first_name")

    return render(
        request,
        "artist/artists-list.html",
        {
            "artists": artists
        }
    )

def editorial(request):
    return render(request, "editorial/editorial-index.html")

def events(request):
    return render(request, "events/events-index.html")
