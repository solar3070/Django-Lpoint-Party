from django.contrib import admin
from django.urls import path, include
import mainapp.views
import eventapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
 
    path('', include('mainapp.urls')),
    path('', include('eventapp.urls')),  
]
