from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('messages/', views.getMessages, name="messages"),
    path('messages/<str:pk>', views.getMessage, name="message"),
]