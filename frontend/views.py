from django.http import HttpResponse
from django.shortcuts import render

from league.models import Pool
from league.serializers import PoolSerializer


def main(request, *args, **kwargs):
    return render(request, 'frontend/main.html')


def supervising_page(request, pool_id):
    if not pool_id:
        return HttpResponse('No pool_id was given!')

    try:
        pool = Pool.objects.get(id=pool_id)
    except Pool.DoesNotExist:
        return HttpResponse('Invalid pool id!')

    return render(request, 'frontend/supervising_page.html', context={
        'pool': PoolSerializer(pool).data
    })
