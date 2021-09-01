from django.urls import path, include
from django.views.generic import TemplateView

from .views import main, supervising_page

app_name = 'react'

urlpatterns = [
    path('', main),
    path('supervising_page/<int:pool_id>', supervising_page)
]
