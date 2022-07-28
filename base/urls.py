from django.urls import path
from . import views

urlpatterns = [
  path('', views.view_home_page, name="home"),
  path('room/<int:pk>/', views.view_room, name="room"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
  path('room/create', views.createRoom, name="room_create"),
  path('register/', views.registerPage, name='register')
]