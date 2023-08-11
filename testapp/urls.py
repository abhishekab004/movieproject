from django.contrib import admin
from django.urls import path
from testapp import views


urlpatterns = [
    path('', views.index_view),
    path('listmovies/', views.list_movies_view),
    path('addmovie/', views.add_movie_view),


]
