# chat/views.py
from django.shortcuts import render


def index(request, user_name):
    return render(request, "chat/index.html", {"user_name": user_name})

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

