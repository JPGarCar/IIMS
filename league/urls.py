from django.urls import path

from .views import home, activity_view, empty_view, pool_view, week_view, day_view

app_name = 'leagues'

urlpatterns = [
    path('home', home, name='home'),
    path('activity/<int:activity_id>', activity_view, name='activity'),
    path('pool/<int:pool_id>', pool_view, name='pool'),
    path('week/<int:week_id>', week_view, name='week'),
    path('day/<int:day_id>', day_view, name='day'),
    path('empy_view', empty_view, name='empty_view')
]
