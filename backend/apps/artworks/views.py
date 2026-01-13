from django.shortcuts import render, get_object_or_404
from .models import Artwork, ArtworkImage

# Create your views here.

def artwork_detail(request, slug):
    artwork = get_object_or_404(
        Artwork.objects
        .select_related("artist")
        .prefetch_related("images"),
        slug = slug
    )

    primary_image = artwork.images.filter(is_primary=True).order_by("order").first()
    other_images = artwork.images.filter(is_primary=False).order_by("order")

    context = {
        "artwork": artwork,
        "primary_image": primary_image,
        "other_images": other_images
    }

    return render(request, "artworks/artwork_detail.html", context)

