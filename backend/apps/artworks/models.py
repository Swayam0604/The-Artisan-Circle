from django.db import models
from django.utils.text import slugify
from apps.accounts.models import ArtistProfile
from django.db.models import Q

# Create your models here.

class Artwork(models.Model):
    artist = models.ForeignKey(
        ArtistProfile,
        on_delete=models.CASCADE,
        related_name="artwork"
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    is_for_sale = models.BooleanField(default=True)
    allow_offers = models.BooleanField(default=True)
    
    is_auction = models.BooleanField(default=False)
    auction_end_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    medium = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)

    height_cm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    width_cm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    year = models.PositiveIntegerField(null=True, blank=True)

    edition_total = models.PositiveIntegerField(null=True, blank=True)
    edition_number = models.PositiveIntegerField(null=True, blank=True)

    is_unique = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Artwork.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.artist}"
    
class ArtworkImage(models.Model):
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE,
        related_name="images"
    )

    images = models.ImageField(upload_to="artworks/")
    is_primary = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        

    def save(self, *args, **kwargs):
        # Handle primary image logic
        if self.is_primary:
            ArtworkImage.objects.filter(
                artwork=self.artwork,
                is_primary=True
            ).exclude(pk=self.pk).update(is_primary=False)

        # Handle order conflicts
        if self.order is not None:
            ArtworkImage.objects.filter(
                artwork=self.artwork,
                order__gte=self.order
            ).exclude(pk=self.pk).update(order=models.F("order") + 1)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.artwork.title}"