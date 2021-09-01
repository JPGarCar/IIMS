from rest_framework import serializers

from match.models import TeamGame, Match, OfficialGame, Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'participant', 'game', 'number', 'score', 'fouls', 'is_mvp']
        depth = 1


class TeamGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamGame
        fields = ['id', 'team', 'score', 'status', 'players', 'get_match']
        depth = 1


class OfficialGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialGame
        fields = ['id', 'status', 'match', 'official']
        depth = 1


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'day', 'time', 'home_team', 'away_team', 'officials')
        depth = 1
