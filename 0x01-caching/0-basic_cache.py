#!/usr/bin/env python3
"""
Basic Caching system module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        Initialize the cache using the parent class initializer.
        """
        super().__init__()

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
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Parameters:
        key (str): The key for the cache item.

        Returns:
        any: The cached item, or None if key is None or key doesn't exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
