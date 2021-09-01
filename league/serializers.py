from rest_framework import serializers

from .models import Pool


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ('name', 'game_duration', 'days_of_play', 'tier', 'term', 'locations_of_play', 'gender')