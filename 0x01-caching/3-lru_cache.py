#!/usr/bin/env python3
"""
LRUCache class module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        Initialize the cache using the parent class initializer.
        """
        super().__init__()
        self.cache_data = OrderedDict()

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
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key, _ = self.cache_data.popitem(last=False)
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

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
