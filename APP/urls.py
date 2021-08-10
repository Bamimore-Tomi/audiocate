from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "APP"

urlpatterns = [
    path("", views.index, name="index"),
    path("homepage.html", views.index, name="index"),
    path("index.html", views.login, name="login"),
    path("login.html", views.login, name="login"),
    path("convert.html", views.convert, name="convert"),
    path("dashboard.html", views.dashboard, name="dashboard"),
    path("explore.html", views.explore, name="explore"),
    path("mybooks.html", views.mybooks, name="mybooks"),
    path("register.html", views.register, name="register"),
    path("genre.html", views.genre, name="genre"),
    path("genre-all.html", views.genre_all, name="genre_all"),
    path("logout.html", views.logout, name="logout"),
    path("contribute.html", views.contribute, name="contribute"),
    path("featured.html", views.featured, name="featured"),
    path("settings.html", views.settings, name="settings")



]
