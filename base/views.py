from django.shortcuts import render, redirect
from .models import Room, Topic
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

def view_home_page(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(description__icontains=q) | Q(name__icontains=q))
  num_rooms = rooms.count()
  topics = Topic.objects.all()
  context = {
    "rooms": rooms, "topics": topics, "num_rooms": num_rooms,
  }
  return render(request, 'base/home.html', context)


def view_room(request, pk):
  print('hello')
  room = Room.objects.get(id=pk)
  context = {
    'room': room
  }

  return render(request, 'base/rooms.html', context)

def registerPage(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      login(request, user)
      return redirect('home')

  form = UserCreationForm()
  context = {
    'form': form
  }

  return render(request, 'base/login_register.html', context)


def loginPage(request):
  page = "login"
  if request.method == "POST":
    print('hello')
    username = request.POST.get("username")
    password = request.POST.get("password")

    try:
      user = User.objects.get(username=username)
    except:
      print('error 1')
      messages.error(request, "User does not exist")

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      print('error 2')
      messages.error(request, "Incorrect Username or Password")

  context = {
    'page': page
  }
  return render(request, 'base/login_register.html', context)

def logoutUser(request):
  logout(request)
  return redirect('home')


def createRoom(request):
  form = RoomForm()
  if request.method == "POST":
    form = RoomForm(request.POST)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.host = request.user
      obj.save()
      return redirect('home')

  context = {
    "form": form
  }
  return render(request, 'base/create_room.html', context)
