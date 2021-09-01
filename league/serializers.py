from rest_framework import serializers

from .models import Gender, Tier, Term, Location, Activity, Pool, Week, Day


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'name']


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ['id', 'name']


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name']


class DaySerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    week = serializers.HyperlinkedRelatedField(
        view_name='week-detail',
        read_only=True
    )

    class Meta:
        model = Day
        fields = ['id', 'day', 'start_time', 'end_time', 'location', 'week']


class WeekSerializer(serializers.ModelSerializer):
    pool = serializers.HyperlinkedRelatedField(
        view_name='pool-detail',
        read_only=True
    )
    days = DaySerializer(many=True)

    class Meta:
        model = Week
        fields = ['id', 'start_date', 'end_date', 'pool', 'days']


class PoolSerializer(serializers.ModelSerializer):
    gender = GenderSerializer()
    tier = TierSerializer()
    term = TermSerializer()
    activity = ActivitySerializer()
    locations_of_play = LocationSerializer(many=True)

    class Meta:
        model = Pool
        fields = ('id', 'name', 'game_duration', 'days_of_play', 'activity', 'gender', 'tier',
                  'term', 'locations_of_play', '__str__')
