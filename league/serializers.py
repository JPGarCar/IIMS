from rest_framework import serializers

from .models import Gender, Tier, Term, Location, Activity, Pool, Week, Day


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['name']


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ['name']


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['name']


class DaySerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    week = serializers.HyperlinkedRelatedField()

    class Meta:
        model = Day
        fields = ['day', 'start_time', 'end_time', 'location', 'week']


class WeekSerializer(serializers.ModelSerializer):
    pool = serializers.HyperlinkedRelatedField()
    days = DaySerializer(many=True)

    class Meta:
        model = Week
        fields = ['start_date', 'end_date', 'pool', 'days']


class PoolSerializer(serializers.ModelSerializer):
    gender = GenderSerializer()
    tier = TierSerializer()
    term = TermSerializer()
    locations_of_play = LocationSerializer(many=True)

    class Meta:
        model = Pool
        fields = ('name', 'game_duration', 'days_of_play', 'activity', 'gender', 'tier',
                  'term', 'locations_of_play', '__str__')
