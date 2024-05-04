from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RoomSerializer
from .models import Room

class RoomList(APIView):
    def get(self, request,location):
        try:
            room = Room.objects.get(location=location)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)
        

    