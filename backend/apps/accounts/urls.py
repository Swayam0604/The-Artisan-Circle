from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.artist_profile_view, name="artist_profile"),
]
