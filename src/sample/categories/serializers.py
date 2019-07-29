# -*- coding: utf-8 -*-
from django.conf import settings

from rest_framework import serializers

from sample.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            return "{}{}".format(
                settings.SITE_URL, obj.image.url
            )

        return None
