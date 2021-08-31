from rest_framework import generics

from match.models import Match
from match.serializers import MatchSerializer


class MatchView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
