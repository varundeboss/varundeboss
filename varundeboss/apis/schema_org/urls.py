from django.conf.urls import url, include

from rest_framework import routers, serializers, viewsets

from . import views

router = routers.DefaultRouter()
router.register(r'schemas', views.SchemaViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='Schema router'),
]