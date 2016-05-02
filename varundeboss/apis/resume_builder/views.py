from django.shortcuts import render
from .models import Resume

from rest_framework import viewsets

from .serializers import ResumeSerializer

# Create your views here.

class ResumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resumes to be created, viewed and edited.
    """
    queryset = Resume.objects.all()#.order_by('-date_joined')
    serializer_class = ResumeSerializer