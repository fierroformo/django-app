# -*- coding: utf-8 -*-
import os
from hashlib import md5

from django.db import models


def get_image_path(instance, filename):
    """
    Get the upload path to images.
    """
    return '{0}/{1}{2}'.format(
        "images",
        md5(filename.encode('utf-8')).hexdigest(),
        os.path.splitext(filename)[-1]
    )


class Category(models.Model):
    """
    Defines model for Category
    """
    name = models.CharField(max_length=255)

    description = models.TextField()

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=get_image_path
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        editable=False,
        blank=True, null=True,
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        editable=False,
        blank=True, null=True,
        auto_now=True
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return "Category: {}".format(self.name)
