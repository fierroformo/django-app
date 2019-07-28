# -*- coding: utf-8 -*-
from drf_yasg import openapi
from drf_yasg.inspectors.view import SwaggerAutoSchema


class CustomJSONAPISchema(SwaggerAutoSchema):

    def get_responses(self):
        """
        Get the possible responses for this view as a swagger
        :class:`.Responses` object.
        :return: the documented responses
        :rtype: openapi.Responses
        """
        response_serializers = self.get_response_serializers()
        response_serializers.update({"400": "BAD REQUEST"})
        response_serializers.update({"403": "FORBIDDEN"})
        response_serializers.update({"404": "NOT FOUND"})
        response_serializers.update({"500": "INTERNAL SERVER ERROR"})
        return openapi.Responses(
            responses=self.get_response_schemas(response_serializers)
        )
