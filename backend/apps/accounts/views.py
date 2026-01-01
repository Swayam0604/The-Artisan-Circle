from django.shortcuts import render, get_object_or_404
from .models import ArtistProfile

# Create your views here.
def home (request):
    return render(request, "home.html")

def artist_profile_view(request, slug):
    artist = get_object_or_404(ArtistProfile, slug=slug)
    return render(request, "artist/profile.html", {"artist": artist})
