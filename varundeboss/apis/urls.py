from django.conf.urls import url, include
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^test/', include('testapp.urls'), name='Test User/Group API'),
    url(r'^resume/', include('apis.jsonresume_org.urls'), name='Json Resume'),
    # url(r'^schema/', include('apis.schema_org.urls'), name='Schemas'),
    url(r'^geoname/', include('apis.geonames_org.urls'), name='Geonames'),
]