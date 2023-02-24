from django.urls import path , include
from . import views
from django.urls import path







urlpatterns = [
    
    path('', views.index),
    
    path('download_video', views.download_video),
    
   
]















