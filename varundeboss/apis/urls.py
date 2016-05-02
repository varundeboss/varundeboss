from django.conf.urls import url, include
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^test/', include('testapp.urls'), name='Test User/Group API'),
    url(r'^resume/', include('apis.resume_builder.urls'), name='Resume Builder'),
]