from rest_framework.serializers import ModelSerializer

from .models import Participant


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'first_name', 'last_name', 'ubc_id', 'signed_waiver', 'status']
