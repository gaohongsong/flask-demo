# -*- coding: utf-8 -*-

from flask import jsonify
from werkzeug.wrappers import Response


class JsonResponse(Response):
    """
        Convert dict response to json response
    """
    default_mimetype = 'text/html'

    @classmethod
    def force_type(cls, response, environ=None):
        """Force dict response to JSON Response
        """
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response, environ)
