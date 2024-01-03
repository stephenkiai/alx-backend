#!/usr/bin/env python3
""" MRUCaching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class, inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Add item in cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove most recently used item
                discarded_key = self.order_used.pop()
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        """ Get item by key
        """
        if key is not None and key in self.cache_data:
            # Update order_used to reflect recent usage
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]

        return None
