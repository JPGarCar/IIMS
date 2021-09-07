from rest_framework import decorators, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from league.models import Gender, Tier, Term, Location, Activity, Day, Week, Pool
from league.serializers import GenderSerializer, TierSerializer, \
    TermSerializer, LocationSerializer, ActivitySerializer, \
    DaySerializer, WeekSerializer, PoolSerializer
from match.models import Match
from match.serializers import MatchSerializer
from participant.models import Participant
from participant.serializers import ParticipantSerializer
from team.serializers import TeamSerializer


class GenderViewSet(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class TierViewSet(ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer


class TermViewSet(ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class DayViewSet(ModelViewSet):
    serializer_class = DaySerializer
    queryset = Day.objects.all()

    # kudos to https://stackoverflow.com/a/37612040 for help with actions with pks
    lookup_field = 'pk'
    lookup_url_kwarg = 'day_pk'

    @decorators.action(methods=['get'], detail=True, url_path='participant/(?P<participant_ubc_id>\d+)')
    def participant(self, request, day_pk, participant_ubc_id):
        day: Day = self.get_object()

        if participant_ubc_id is None:
            return Response(data={'error': 'No participant id given!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            participant = Participant.objects.get(ubc_id=participant_ubc_id)
        except Participant.DoesNotExist:
            return Response(data={'error': 'No participant found with given ID!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            match = day.matches.get(away_team__team__team_roster=participant.pk)
            team = match.away_team.team
        except (Match.DoesNotExist, Participant.DoesNotExist):
            try:
                match = day.matches.get(home_team__team__team_roster=participant.pk)
                team = match.home_team.team
            except (Match.DoesNotExist, Participant.DoesNotExist):
                match = participant = team = None

        if match is None:
            return Response(data={'error': 'Participant not playing today!'}, status=status.HTTP_404_NOT_FOUND)
        else:
            participant_serializer = ParticipantSerializer(participant)
            match_serializer = MatchSerializer(match)
            team_serializer = TeamSerializer(team)
            return Response(data={
                'participant': participant_serializer.data,
                'match': match_serializer.data,
                'team': team_serializer.data,
            })


class WeekViewSet(ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class PoolViewSet(ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
