from django.shortcuts import render
from .models import Thing

from rest_framework import viewsets

from .serializers import SchemaSerializer

# Create your views here.

class SchemaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resumes to be created, viewed and edited.
    """
    queryset = Thing.objects.all()#.order_by('-date_joined')
    serializer_class = SchemaSerializer