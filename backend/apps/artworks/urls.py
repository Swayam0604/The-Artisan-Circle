# apps/artworks/urls.py
from django.urls import path   
from .import views
from .views import artwork_detail

app_name = "artworks"

urlpatterns = [
    path("<slug:slug>/", artwork_detail, name="artwork-detail"),

]
