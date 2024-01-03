#!/usr/bin/env python3
""" BasicCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
    """

    def put(self, key, item):
        """ Add item in cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get item by key
        """
        if key is not None:
            return self.cache_data.get(key)
