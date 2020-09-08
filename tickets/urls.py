from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.home, name="main"),
    path("search/", views.searchView, name="search"),
    # path("visual/", views.visualView, name="visual"),
]