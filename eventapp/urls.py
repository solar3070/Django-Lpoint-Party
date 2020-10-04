from django.urls import path
from . import views

urlpatterns = [
    path('', views.event1, name="event1"),
    path('', views.event2, name="event2"),
    path('index/', views.index,name='index'),
    path('create/', views.post_create,name='create'),
    path('event_post/<int:post_id>/', views.post_detail,name='detail'),
    path('update/<int:post_id>/', views.post_update,name='update'),
    path('delete/<int:post_id>/',views.post_delete,name='delete'),
    ]
