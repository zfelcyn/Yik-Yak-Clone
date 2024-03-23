from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .messages import messages  # Assuming messages is a list defined elsewhere

@api_view(['GET'])
def getRoutes(request): 
    routes = [
        '/api/messages',
        '/api/messages/create/',
        '/api/messages/upload/',
        '/api/messages/<id>/reviews/',
        '/api/messages/top/',
        '/api/messages/<id>/',
        '/api/messages/delete/<id>',
        '/api/messages/update/<id>',
    ]
    return Response(routes)

@api_view(['GET'])
def getMessages(request):
    return Response(messages)  # Remove safe=False since it's not needed

#TODO Make messages be encyption key 
@api_view(['GET'])
def getMessage(request, pk):
    message = None
    for i in messages: 
        if i['_id'] == pk:
            message = i 
            break

    return Response(message)  # Remove safe=False since it's not needed

