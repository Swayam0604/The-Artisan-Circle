from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,ArtistProfile

@receiver(post_save,sender=User)
def create_artist_profile(sender, instance, created, **kwargs):
    if created and instance.role == "artist":
        ArtistProfile.objects.create(
            user=instance,
            first_name="",
            last_name="",
            )
