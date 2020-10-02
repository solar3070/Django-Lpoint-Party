from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('eventIntro/', views.eventIntro, name="eventIntro"),
    path('event1/', views.event1, name="event1"),
    path('event2/', views.event2, name="event2"),
]