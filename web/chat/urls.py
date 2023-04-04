from django.urls import path

from . import views

urlpatterns = [
    path("index<str:user_name>", views.index, name='index'),
    path("room<str:room_name>/", views.room, name="room"),
]