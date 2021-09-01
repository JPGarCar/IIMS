from rest_framework.viewsets import ModelViewSet

from league.models import Gender, Tier, Term, Location, Activity, Day, Week, Pool
from league.serializers import GenderSerializer, TierSerializer, \
    TermSerializer, LocationSerializer, ActivitySerializer, \
    DaySerializer, WeekSerializer, PoolSerializer


class GenderViewSet(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class TierViewSet(ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer


class TermViewSet(ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class DayViewSet(ModelViewSet):
    serializer_class = DaySerializer
    queryset = Day.objects.all()


class WeekViewSet(ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class PoolViewSet(ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
