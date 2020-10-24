from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list,name='list'),
    path('create/', views.post_create,name='create'),
    path('event_post/<int:post_id>/', views.post_detail,name='detail'),
    path('update/<int:post_id>/', views.post_update,name='update'),
    path('delete/<int:post_id>/',views.post_delete,name='delete'),
]

