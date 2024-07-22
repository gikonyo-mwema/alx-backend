#!/usr/bin/env python3
"""
Function to calculate the start and end indices for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two - start and end index corresponding
    to the range to return in a list for those pagination parameters

    Parameters:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
