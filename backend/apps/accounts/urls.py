from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.artist_detail_view, name="artist_detail"),
]
