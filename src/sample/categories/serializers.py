# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from sample.categories.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
