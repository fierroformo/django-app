# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from sample.api import urls as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_urls, 'api'), namespace='api')),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
