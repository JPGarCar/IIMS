from rest_framework.viewsets import ModelViewSet

from match.models import Player, TeamGame, OfficialGame, Match
from match.serializers import PlayerSerializer, TeamGameSerializer,\
    OfficialGameSerializer, MatchSerializer


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamGameViewSet(ModelViewSet):
    queryset = TeamGame.objects.all()
    serializer_class = TeamGameSerializer


class OfficialGameViewSet(ModelViewSet):
    queryset = OfficialGame.objects.all()
    serializer_class = OfficialGameSerializer


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
