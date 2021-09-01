from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from league.models import Activity, Pool, Week, Day


@login_required
def home(request):
    if request.method == 'GET':
        activities = Activity.objects.all()

        return render(request, 'league/league_home.html', context={
            'activities': activities
        })


@login_required
def activity_view(request, activity_id):
    if activity_id is None:
        return HttpResponseBadRequest('No activity ID given.')
    if request.method == 'GET':
        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            return HttpResponseBadRequest('Activity id given is not valid!')

        return render(request, 'league/activity_view.html', context={
            'activity': activity,
            'pools': activity.pools.all()
        })


@login_required
def pool_view(request, pool_id):
    if pool_id is None:
        return HttpResponseBadRequest('No pool id given!')
    if request.method == 'GET':
        try:
            pool = Pool.objects.get(id=pool_id)
        except Pool.DoesNotExist:
            return HttpResponseBadRequest('Pool id given is invalid!')

        locations = ''
        for location in pool.locations_of_play.all():
            locations += location.name + ', '

        return render(request, 'league/pool_view.html', context={
            'pool': pool,
            'weeks': pool.weeks.all(),
            'teams': pool.team_set.all(),
            'locations': locations,
            'days_of_play': pool.get_days_of_play_display()
        })


@login_required
def week_view(request, week_id):
    if week_id is None:
        return HttpResponseBadRequest('No week id given!')
    if request.method == 'GET':
        try:
            week = Week.objects.get(id=week_id)
        except Week.DoesNotExist:
            return HttpResponseBadRequest('Week id given is invalid!')

        days = week.days.all()

        return render(request, 'league/week_view.html', context={
            'week': week,
            'days_of_play': days,
        })


@login_required
def day_view(request, day_id):
    if day_id is None:
        return HttpResponseBadRequest('No day id given!')
    if request.method == 'GET':
        try:
            day = Day.objects.get(id=day_id)
        except Day.DoesNotExist:
            return HttpResponseBadRequest('Day id given is invalid!')

        matches = day.match_set.all()

        return render(request, 'league/day_view.html', context={
            'day': day,
            'matches': matches
        })


@login_required
def empty_view(request):
    return HttpResponse('TODO')
