from rest_framework import serializers

from match.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'day', 'time', 'home_team', 'away_team', )

