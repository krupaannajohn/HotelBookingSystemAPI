from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer

from .models import Room

"""def search_rooms_by_location(location):
    return Room.objects.filter(location=location, available=True)
"""

class RoomList(APIView):
    def get(self, request,location):
        try:
            room = Room.objects.get(location=location)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)
        # return Response(serializer.data)

    """def post(self, request):
        location = request.data.get('location')  # Assuming location is sent in the request data
        if location:
            rooms = search_rooms_by_location(location)
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Location parameter missing in request data"}, status=status.HTTP_400_BAD_REQUEST)"""