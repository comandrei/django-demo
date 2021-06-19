from dj.siit.curs.models import Student
from rest_framework import viewsets

from .serializers import CursSerializer
from curs.models import Curs

class CursViewSet(viewsets.ModelViewSet):
    queryset = Curs.objects.all()
    serializer_class = CursSerializer
