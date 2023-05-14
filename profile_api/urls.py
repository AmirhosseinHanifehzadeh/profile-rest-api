from django.urls import path 
from profile_api import views


urlpatters = [
    path('hello-view/', views.HelloApiView.as_view()), 
]