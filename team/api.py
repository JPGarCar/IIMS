from rest_framework.viewsets import ModelViewSet

from .serializers import UnitSerializer, TeamSerializer
from .models import Unit, Team


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
