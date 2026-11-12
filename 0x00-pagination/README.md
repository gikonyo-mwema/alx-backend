# 0x00. Pagination

This project builds pagination helpers and a server that reads from the
`Popular_Baby_Names.csv` dataset.

## Tasks

| Task | Implementation | Driver |
| --- | --- | --- |
| 0. Simple helper function: calculate the start and end indexes for a page | [0-simple_helper_function.py](./0-simple_helper_function.py) | [0-main.py](./0-main.py) |
| 1. Simple pagination: return a page from the dataset | [1-simple_pagination.py](./1-simple_pagination.py) | [1-main.py](./1-main.py) |
| 2. Hypermedia pagination: include page metadata and navigation details | [2-hypermedia_pagination.py](./2-hypermedia_pagination.py) | [2-main.py](./2-main.py) |
| 3. Deletion-resilient hypermedia pagination: preserve results as rows are removed | [3-hypermedia_del_pagination.py](./3-hypermedia_del_pagination.py) | [3-main.py](./3-main.py) |

## Data

- [Popular_Baby_Names.csv](./Popular_Baby_Names.csv) is the dataset used by the
  pagination server.
