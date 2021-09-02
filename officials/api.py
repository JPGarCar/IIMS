from rest_framework.viewsets import ModelViewSet

from .serializers import OfficialSerializer
from .models import Official


class OfficialViewSet(ModelViewSet):
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer
