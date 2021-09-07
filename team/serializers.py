from rest_framework.serializers import ModelSerializer

from participant.serializers import ParticipantSerializer
from .models import Unit, Team


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'team_number', 'pool', 'unit', 'secondary_unit', 'team_roster', 'team_captain']
        depth = 1
