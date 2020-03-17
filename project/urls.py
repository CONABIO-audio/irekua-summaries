from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^summaries/', include('irekua_summaries.urls')),
]
