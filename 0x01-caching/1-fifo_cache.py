#!/usr/bin/env python3
"""
FIFOCache class module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        Initialize the cache using the parent class initializer.
        """
        super().__init__()
        self.order = []

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

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = self.order.pop(0)
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")

        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)

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
        return self.cache_data[key]
