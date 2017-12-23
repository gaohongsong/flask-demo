# -*- coding: utf-8 -*-

from werkzeug.routing import BaseConverter
from werkzeug.urls import url_quote, url_unquote


class ListConverter(BaseConverter):
    """Base class for all converters."""

    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = url_unquote(separator)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(map(str, values))
        # return self.separator.join(super(ListConverter, self).to_url(v) for v in values)
