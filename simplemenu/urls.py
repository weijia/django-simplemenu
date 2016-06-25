from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import models

urlpatterns = patterns('',
                       )
try:
    from django_auto_filter.views_django_auto_filter_new import DjangoAutoFilterNew
    urlpatterns += [url(r'^$', login_required(
        DjangoAutoFilterNew.as_view(
            model=models.MenuItem,
        )))]
except ImportError:
    pass


try:
    from djangoautoconf.django_rest_framework_utils.serializer_generator import add_all_urls
    add_all_urls(urlpatterns, models)
except ImportError:
    pass
