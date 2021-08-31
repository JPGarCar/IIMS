from django.urls import path, include

from match.api import MatchView

app_name = 'match'

# kudos to https://www.webforefront.com/django/consolidatedjangourls.html for help
# on url consolidation, can use include with list of url patterns
api_urlpatterns = [
    path('all_matches', MatchView.as_view(), name='all_matches')
]

urlpatterns = [
    path('api/', include(api_urlpatterns), name='api')
]
