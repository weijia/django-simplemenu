from django.conf.urls import patterns, include, url
from djangoautoconf.django_rest_framework_utils.serializer_generator import add_all_urls
import models


urlpatterns = patterns('',
                       )

add_all_urls(urlpatterns, models)
