from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from match.models import Match
from match.serializers import MatchSerializer


class MatchView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
