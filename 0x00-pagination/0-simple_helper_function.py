#!/usr/bin/env python3
""" A helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns a tuple of size two containing start & end index"""
    if page <= 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size
    # page starting and ending index
    end_index = page * page_size
    return start_index, end_index
