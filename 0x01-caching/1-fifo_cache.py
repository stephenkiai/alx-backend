#!/usr/bin/env python3
""" FIFOCaching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class, inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove first item put in cache
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get item by key
        """
        if key is not None:
            return self.cache_data.get(key)
