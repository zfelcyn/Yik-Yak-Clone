from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Message

@csrf_exempt
def join_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')

        if Room.objects.filter(name=room_name).exists():
            return redirect(f'/{room_name}/?username={username}')
        else:
            new_room = Room.objects.create(name=room_name)
            new_room.save()
            return redirect(f'/{room_name}/?username={username}')
    return HttpResponse('Invalid method')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room_name = request.POST.get('room_name')
        message = request.POST.get('message')

        # Retrieve the room object
        room = Room.objects.get(name=room_name)

        # Save the message to the database
        new_message = Message.objects.create(user=username, room=room, value=message)
        new_message.save()

        return HttpResponse('Message sent successfully')
    return HttpResponse('Invalid method')

def get_messages(request, room_name):
    # Retrieve the room object
    room = Room.objects.get(name=room_name)

    # Retrieve messages for the specified room from your database
    messages = Message.objects.filter(room=room)

    # Serialize messages and return as JSON response
    serialized_messages = [{'user': message.user, 'value': message.value} for message in messages]
    return JsonResponse({'messages': serialized_messages})

