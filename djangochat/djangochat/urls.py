from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_login(request):
    return redirect('/login/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_login),
    path('', include('chat.urls'))
]
