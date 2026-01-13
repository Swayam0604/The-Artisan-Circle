# apps/accounts/views.py
from django.shortcuts import render, get_object_or_404
from .models import ArtistProfile
from apps.artworks.models import Artwork
# Create your views here.

def artist_detail_view(request, slug):
    artist = get_object_or_404(ArtistProfile, slug=slug)

    artworks = (
        Artwork.objects
        .filter(artist=artist)
        .prefetch_related("images")
        .order_by("-created_at")
    )

    return render(
        request,
        "artist/artist-detail.html",
        {
            "artist": artist,
            "artworks": artworks
        }
    )


