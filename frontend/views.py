from django.http import HttpResponse
from django.shortcuts import render

from league.models import Pool, Week, Day
from league.serializers import PoolSerializer, WeekSerializer, DaySerializer


def main(request, *args, **kwargs):
    return render(request, 'frontend/main.html')


def supervising_page(request, pool_id, week_id, day_id):
    try:
        pool = Pool.objects.get(id=pool_id)
    except Pool.DoesNotExist:
        return HttpResponse('Invalid pool id!')

    try:
        week = Week.objects.get(id=week_id)
    except Week.DoesNotExist:
        return HttpResponse('Invalid week id!')

    try:
        day = Day.objects.get(id=day_id)
    except Day.DoesNotExist:
        return HttpResponse('Invalid day id!')

    return render(request, 'frontend/supervising_page.html', context={
        'pool': PoolSerializer(pool).data,
        'week': WeekSerializer(week).data,
        'day': DaySerializer(day).data
    })
