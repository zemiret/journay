from rest_framework import viewsets, views

from core.models import Journey
from core.serializers import JourneySerializer


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer


class DayEntryView(views.APIView):
    pass
