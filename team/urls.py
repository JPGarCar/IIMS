from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import UnitViewSet, TeamViewSet

app_name = 'team'

router = DefaultRouter()
router.register('teams', TeamViewSet)
router.register('units', UnitViewSet)

# kudos to https://www.webforefront.com/django/consolidatedjangourls.html for help
# on url consolidation, can use include with list of url patterns
api_urlpatterns = [

]

api_urlpatterns = api_urlpatterns + router.urls

urlpatterns = [
    path('api/', include((api_urlpatterns, 'api'), namespace='api'))
]
