from django.conf.urls import url, include
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets

from . import views

router = routers.DefaultRouter()
router.register(r'resumes', views.ResumeViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='Resume router'),
]