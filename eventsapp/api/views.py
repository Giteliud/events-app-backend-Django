from rest_framework import viewsets
from ..models import Event
from .serializers import EventModelSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer