from django.urls import path
from . import views

urlpatterns = [
    path('', views.event1, name="evnet1"),
    path('', views.event2, name="evnet2"),
]