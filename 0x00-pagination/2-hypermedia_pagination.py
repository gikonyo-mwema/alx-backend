#!/usr/bin/env python3
"""
Function to calculate the start and end indices for pagination.
"""

import csv
from typing import List, Tuple, Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Parameters:
        - page (int): The current page number (1-indexed).
        - page_size (int): The number of items per page.

        Returns:
        - List[List]: A list of lists containing
        the rows for the specified page.
        """
        assert type(page) == int and type(page_size) == int
        assert (page > 0 and page_size > 0)
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index > len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset with hypermedia information.

        Parameters:
        - page (int): The current page number (1-indexed).
        - page_size (int): The number of items per page.

        Returns:
        - Dict: A dictionary containing pagination information and the data.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        hyper = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyper
