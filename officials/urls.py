from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import OfficialViewSet

app_name = 'officials'

router = DefaultRouter()
router.register('officials', OfficialViewSet)

# kudos to https://www.webforefront.com/django/consolidatedjangourls.html for help
# on url consolidation, can use include with list of url patterns
api_urlpatterns = [

]

api_urlpatterns = api_urlpatterns + router.urls

urlpatterns = [
    path('api/', include(api_urlpatterns), name='api')
]
