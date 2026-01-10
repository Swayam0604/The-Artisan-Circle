# apps/artworks/urls.py
from django.urls import path   
from .import views
from .views import artwork_detail, artwork_list

app_name = "artworks"

urlpatterns = [
    path("<slug:slug>/", artwork_detail, name="artwork-detail"),
    path("", views.artwork_list, name="artwork-list"),

]
