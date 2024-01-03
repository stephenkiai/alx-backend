#!/usr/bin/env python3
""" LFUCaching module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class,inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}
        self.order_used = []  # track the order of usage

    def put(self, key, item):
        """ Add item in cache using LFU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find least frequency used item(s)
                min_frequency = min(self.frq.values())
                l_f_k = [k for k, v in self.frq.items() if v == min_frequency]

                # use LRU to break tie if more than 1 item has least frequency
                if len(l_f_k) > 1:
                    l_r_u = min(l_f_k, key=lambda k: self.order_used.index(k))
                    l_f_k = [l_r_u]

                # Remove least frequency used item
                discarded_key = l_f_k[0]
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                self.order_used.remove(discarded_key)
                # Remove from order_used
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            # Add to order_used
            self.order_used.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Update frequency and order_used to reflect recent usage
            self.frequency[key] += 1
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]

        return None
