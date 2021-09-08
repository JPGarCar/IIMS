from rest_framework import decorators, status
from rest_framework.response import Response
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

    @decorators.action(methods=['post'], detail=True)
    def sign_in(self, request, pk):
        data = request.data
        team_game: TeamGame = self.get_object()

        participant_pk = data.get('participant_pk', None)
        participant_number = data.get('participant_number', None)

        if participant_pk is None:
            return Response(data={'error': 'No participant id given!'}, status=status.HTTP_400_BAD_REQUEST)

        is_complete = team_game.add_participant(participant_pk=participant_pk, participant_number=participant_number)

        if is_complete:
            return Response(data={'status': 'Participant was added to the team match!'})
        else:
            return Response(
                data={'error': 'Participant was not added to the team match!'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class OfficialGameViewSet(ModelViewSet):
    queryset = OfficialGame.objects.all()
    serializer_class = OfficialGameSerializer


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
