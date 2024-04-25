# BY FAR THE MOST IMPORTANT FILE HERE!!!!!

from django.shortcuts import render, redirect # imports render and redirect from django shortcuts module, render combines a given template with a context dictionary
# and returns an HttpResponse with that renderred text, while redirect is a utility to redirect the user to a different URL
# Imports room and message models from the models.py file in the chat file, models define
# the database schema fro the chatrooms and messages
from chat.models import Room, Message, FriendRequest, Friendship, CustomUser
#imports httpresponse and json response from djangos http module,
# httpresponse is used to pass the response back to the web browser, and jsonresponse
# is a subclass of httpresponse that helps to create a json encoded response
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here. Takes a http response and returns an http response, landing page of the chat app
def home(request):
    return render(request, 'login.html')

# handles the logic of joining teh chat room
def room(request, room):
    # extracts username from the get request parameters
    username = request.user.username
    if (username):
        print(username)
    else:
        print("wrgindfosjdndgfcgvdfseindgvcfdskopjidg")
    # queries the room model for a room with the given name and stores it in
    # room_details. This retrieves info about the chat room from the database
    room_details  = get_object_or_404(Room, name=room)
    # renders room.html template, passing in username, room name, and room_details for context to the template
    # this is teh main chat room page where messages are displayed
    return render(request, 'room.html', {
        'username' : username,
        'room' : room,
        'room_details' : room_details
    })

# This function checks if the room exists when attempting to create or join a room.
def checkview(request):
    # retrives the room name and username from the POST request data
    room = request.GET.get('room_name')
    # form_class = CustomAuthenticationForm
    # form = self.form_class(request.POST)
    # user = form.save()
    # login(request,user)

    username = request.GET.get('username')

    print(room)
    print(username)

    # checks if the room exists in the database
    if Room.objects.filter(name=room).exists():
        # redirects user to the room URL, with the username as a GET parameter
        return redirect('/'+room+'/?username='+username)

    else:
        # if the room doesnt exist, saves it to the database and redirects the user to the new room URL, with the username as a GET parameter
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

# defines a send view funvtion for the handling of sending messages within the chat room
def send(request):
    # retrieves the message, username, and room_id from the POST request data
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    #  creates a new message object with the provided message, username, and room ID, then saves it 
    # to the database.
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    # returns an httpresponse indicating that the message was sent 
    return HttpResponse('Message sent successfully')

#defines a getMessages view function that retrieves messages for a specific chat room
def getMessages(request, room):
    # queries the room model to get the details of the room with the given name
    room_details = Room.objects.get(name=room)
    # retrieves all message objects asscociated with the room id 
    messages = Message.objects.filter(room=room_details.id)
    # returns a json response containing a list of messages, used to fetch messages
    # in real time for display in the chat room
    return JsonResponse({"messages":list(messages.values())})



class RegisterView(View):
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        print("test1")
        form = self.form_class()
        return render(request, 'register.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        print("test2")
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page or wherever you like
        return render(request, 'register.html', {'form': form})
    
# class CustomLoginView(LoginView):
#     print("hello")
#     form_class = CustomAuthenticationForm
#     template_name = 'login.html'

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             print(username)
#             password = form.cleaned_data.get('password')
#             print(password)
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('checkview')
#         return self.form_invalid(form)

from django.urls import reverse

class CustomLoginView(LoginView):
    print("hello")
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                room_name = request.GET.get('room_name')
                login(request, user)
                # Redirect to 'checkview' with URL parameters
                return redirect(reverse('checkview') + f'?username={username}&room_name={room_name}')
        return self.form_invalid(form)
  

class CustomLogoutView(LogoutView):
    next_page = 'home'  # Redirect to home page or login page

# View for sending a friend request
@login_required
def send_friend_request(request):
    if request.method == 'POST':
        # Retrieve the receiver_id from the POST data
        receiver_id = request.POST.get('receiver_id')
        
        if receiver_id is None:
            return HttpResponseBadRequest("Receiver ID is missing in the request.")
        
        # Get the receiver user object
        receiver = get_object_or_404(CustomUser, id=receiver_id)
        
        if receiver is None:
            return HttpResponseBadRequest("Receiver user does not exist.")
        
        # Check if a friend request already exists or if users are already friends
        if FriendRequest.objects.filter(sender=request.user, receiver=receiver).exists() or Friendship.objects.filter(user1=request.user, user2=receiver).exists():
            return HttpResponse("Friend request already sent or users are already friends.")
        
        # Create and save the friend request
        friend_request = FriendRequest(sender=request.user, receiver=receiver, status='pending')
        friend_request.save()
        
        return HttpResponse("Friend request sent successfully.")
    else:
        # Handle the case when the request method is not POST
        return HttpResponseBadRequest("Invalid request method.")

# View for accepting or rejecting a friend request
@login_required
def handle_friend_request(request, request_id):
    # Get the friend request object
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    
    # Check if the current user is the receiver of the request
    if request.user == friend_request.receiver:
        # Update the status of the friend request based on the action (accept/reject)
        action = request.POST.get('action')
        if action == 'accept':
            friend_request.status = 'accepted'
            # Create a friendship between the sender and receiver
            friendship = Friendship(user1=friend_request.sender, user2=friend_request.receiver)
            friendship.save()
        elif action == 'reject':
            friend_request.status = 'rejected'
        friend_request.save()
        return HttpResponse("Friend request handled successfully.")
    else:
        return HttpResponse("You are not authorized to handle this friend request.")

# View for displaying friend requests
@login_required
def view_friend_requests(request):
    # Get the ID of the current user
    receiver_id = request.user.id
    
    # Get all friend requests received by the current user
    friend_requests = FriendRequest.objects.filter(receiver=request.user, status='pending')
    
    # Get all friend requests sent to the current user
    incoming_requests = FriendRequest.objects.filter(sender=request.user, status='pending')
    
    # Pass friend requests and receiver_id to the template context
    return render(request, 'friend_requests.html', {'friend_requests': friend_requests, 'receiver_id': receiver_id, 'incoming_requests': incoming_requests})

# View for displaying the list of friends
@login_required
def view_friends(request):
    # Assuming the logged-in user is stored in request.user
    user = request.user
    
    # Fetch all friendships where the logged-in user is either user1 or user2,
    # excluding friendships where the logged-in user is both user1 and user2
    user_friends = Friendship.objects.filter(user1=user) | Friendship.objects.filter(user2=user)
    
    return render(request, 'friends_list.html', {'user_friends': user_friends})