# -*- coding: utf-8 -*-
from drf_yasg.utils import swagger_auto_schema

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from sample.categories.models import Category
from sample.categories.serializers import CategorySerializer
from sample.utils.schemas import CustomJSONAPISchema


class CategoryViewSet(
    ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    swagger_schema = CustomJSONAPISchema
