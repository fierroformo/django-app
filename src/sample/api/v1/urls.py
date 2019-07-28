# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter, SimpleRouter

from sample.categories.viewsets import CategoryViewSet


# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet)

"""
router = SimpleRouter()
router.register(
    r'categories',
    CategoryViewSet,
    base_name='categories-list'
)
"""

urlpatterns = router.urls
