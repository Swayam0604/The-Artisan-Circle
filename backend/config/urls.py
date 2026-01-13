# config/urls/
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("artworks/", views.artwork_list, name="artwork-list"),
    path("artwork/", include("apps.artworks.urls")),
    path("artists/", views.artists_list, name="artist-list"),  # LIST
    path("artist/", include("apps.accounts.urls")),
    path("editorial/", views.editorial, name="editorial"),
    path("events/", views.events, name="events"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=None)
    