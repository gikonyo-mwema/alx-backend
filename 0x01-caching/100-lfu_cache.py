#!/usr/bin/env python3
"""
LFUCache class module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        Initialize the cache using the parent class initializer.
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        Parameters:
        key (str): The key for the cache item.
        item (any): The item to cache.

        If key or item is None, the method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
            del self.usage_order[key]
        self.cache_data[key] = item
        self.frequency[key] += 1
        self.usage_order[key] = None

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
            if len(lfu_keys) > 1:
                discard_key = next(iter(self.usage_order))
            else:
                discard_key = lfu_keys[0]
            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            del self.usage_order[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.

        Parameters:
        key (str): The key for the cache item.

        Returns:
        any: The cached item, or None if key is None or key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]
