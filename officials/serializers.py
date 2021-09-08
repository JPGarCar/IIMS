from rest_framework.serializers import ModelSerializer
from .models import Official


class OfficialSerializer(ModelSerializer):
    class Meta:
        model = Official
        fields = ['id', 'first_name', 'last_name', 'level']
