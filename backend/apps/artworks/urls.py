from django.urls import path
from .views import artwork_detail

app_name = "artworks"

urlpatterns = [
    path("<slug:slug>/", artwork_detail, name="artwork-detail"),
]
