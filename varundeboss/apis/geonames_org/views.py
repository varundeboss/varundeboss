from django.shortcuts import render
from .models import Geoname

from rest_framework import viewsets

from .serializers import GeonameSerializer

# Create your views here.

class GeonameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resumes to be created, viewed and edited.
    """
    queryset = Geoname.objects.all()#.order_by('-date_joined')
    serializer_class = GeonameSerializer