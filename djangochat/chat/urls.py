from django.urls import path # imports path funmction from django library
from . import views # imports views from local files, each view functionr returns an http result
from .views import RegisterView, CustomLoginView, CustomLogoutView

# url patterns are something that django uses to route incomming http requests to the appropritate view
# based on the requests url path. An http request is a message sent by a client to a server,\
# asking for some action to be performed on the server. Each http request includes a method, like  the action type(GET to submit data, PUT to update resoure, and DELETE to remove stuff)
# URL, or uniform resource locator, specifies the path to the resource on the server, headers provide additional info like content type, authetication tokens, ect. Finally theres the body, which contains data sent
# with the request.

# A view in context of django, is a python function that takes an http request as input and returns an http result
# Logic in this can include accessing data from the database, processing or transforming data, or deciding what to send back, like a html page,
# json, xml, redirect, whatever. A VIEW FUNCTION IS THE AIR TRAFFIC CONTROL OF THE BACKEND 
urlpatterns = [
    # matches an empty string representing the root URL of the website, and route those requests to the home function
    # in the views module. The name = 'home' assigns a name to the url, which we can type in the website url
    path('login/',CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('login/checkview/',views.checkview, name='login2'),
    # dynamic segment <str:room> matches any string and passes a room argum,ent, hekpful for creating urls based on username
    path('<str:room>/', views.room,name='room'),
    # path that leads to checkview, will explain this more in .views
    path('checkview', views.checkview, name='checkview'),
    # also for the send function, same stuff
    path('send', views.send, name='send'),
    # dynamic url pattern that fetches messages for a single room
    path('getMessages/<str:room>/', views.getMessages,name='getMessages'),

]