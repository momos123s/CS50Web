from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/",views.wiki, name = "wiki"),
    path("search", views.search, name = "search" ),
    path("new_wiki", views.new_page , name = "new_page"),
    path("edit_page/<str:entry>/", views.edit_page, name= "edit_page"),
    path("random", views.random_wiki, name = "random")
]
