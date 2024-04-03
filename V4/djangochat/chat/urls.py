from django.contrib import admin
from django.urls import path
from chat import views  # Assuming views.py is in the chat app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Maps to the home view in views.py
    path('<str:room>/', views.room, name='room'),  # Maps to the room view with a dynamic room parameter
    path('checkview/', views.checkview, name='checkview'),  # Maps to the checkview view in views.py
    path('send/', views.send, name='send'),  # Maps to the send view in views.py
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),  # Maps to the getMessages view with a dynamic room parameter
]

