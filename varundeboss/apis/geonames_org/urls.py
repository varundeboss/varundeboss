from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'geonames', views.GeonameViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='Geoname router'),
]