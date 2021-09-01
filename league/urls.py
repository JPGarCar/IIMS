from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import home, activity_view, empty_view, pool_view, week_view, day_view
from .api import GenderViewSet, TierViewSet, TermViewSet, LocationViewSet, \
    ActivityViewSet, DayViewSet, WeekViewSet, PoolViewSet

app_name = 'leagues'

router = DefaultRouter()
router.register('genders', GenderViewSet)
router.register('tiers', TierViewSet)
router.register('terms', TermViewSet)
router.register('locations', LocationViewSet)
router.register('activities', ActivityViewSet)
router.register('days', DayViewSet)
router.register('weeks', WeekViewSet)
router.register('pools', PoolViewSet)

api_urlpatterns = [

]

api_urlpatterns = api_urlpatterns + router.urls

urlpatterns = [
    path('home', home, name='home'),
    path('activity/<int:activity_id>', activity_view, name='activity'),
    path('pool/<int:pool_id>', pool_view, name='pool'),
    path('week/<int:week_id>', week_view, name='week'),
    path('day/<int:day_id>', day_view, name='day'),
    path('empy_view', empty_view, name='empty_view'),
    path('api/', include(api_urlpatterns), name='api'),
]
