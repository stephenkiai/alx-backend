#!/usr/bin/env python3
""" LIFOCaching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class, inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add item in cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove last item put in cache
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get item by key
        """
        if key is not None:
            return self.cache_data.get(key)
