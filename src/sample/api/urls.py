# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import AllowAny


urlpatterns = [
    path('v1/', include(('sample.api.v1.urls', 'v1'), namespace='v1')),
]


if not settings.PRODUCTION:
    schema_view = get_schema_view(
       openapi.Info(
          title="SAMPLE API",
          default_version='v1',
          description="API for Sample APP",
          terms_of_service="https://www.google.com/policies/terms/",
          contact=openapi.Contact(email="fierroformo@gmail.com"),
          license=openapi.License(name="BSD License"),
       ),
       url=settings.DEFAULT_API_URL,
       validators=['flex'],
       public=True,
       permission_classes=(AllowAny,),
    )
    urlpatterns += [
        path(
            'swagger(<str:format>\.json|\.yaml)',
            schema_view.without_ui(cache_timeout=None), name='schema-json'
        ),
        path(
            'swagger',
            schema_view.with_ui('swagger', cache_timeout=None),
            name='schema-swagger-ui'
        ),
        path(
            'redoc',
            schema_view.with_ui('redoc', cache_timeout=None),
            name='schema-redoc'
        ),
    ]
