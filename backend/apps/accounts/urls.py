# apps/accounts/urls.py
from django.urls import path
from .views import artist_detail_view

app_name = "accounts"

urlpatterns = [
    path("<slug:slug>/", artist_detail_view, name="artist-detail"),  # /artist/<slug>/
]
