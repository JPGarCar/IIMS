from django.urls import path, include
from rest_framework.routers import DefaultRouter

from match.api import PlayerViewSet, TeamGameViewSet, OfficialGameViewSet, MatchViewSet

app_name = 'match'

router = DefaultRouter()
router.register('players', PlayerViewSet)
router.register('team_games', TeamGameViewSet)
router.register('official_games', OfficialGameViewSet)
router.register('matches', MatchViewSet)

# kudos to https://www.webforefront.com/django/consolidatedjangourls.html for help
# on url consolidation, can use include with list of url patterns
api_urlpatterns = [

]

api_urlpatterns = api_urlpatterns + router.urls

urlpatterns = [
    path('api/', include((api_urlpatterns, 'api'), namespace='api'))
]