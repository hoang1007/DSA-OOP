from typing import List

from .functional import swap, Comparator
from .type import Comparable


def bubble_sort(data: List[Comparable], descending: bool = False):
    comparator = Comparator(descending)
    has_swap_op = True

    while has_swap_op:
        has_swap_op = False
        for i in range(len(data) - 1):
            if comparator.less_than(data[i + 1], data[i]):
                swap(data, i, i + 1)
                has_swap_op = True

    return data


def insertion_sort(data: List[Comparable], descending: bool = False):
    comparator = Comparator(descending)

    for i in range(1, len(data)):
        cur_val = data[i]
        for j in range(i - 1, -2, -1):
            if j >= 0 and comparator.less_than(cur_val, data[j]):
                data[j + 1] = data[j]
            else:
                data[j + 1] = cur_val
                break

    return data


def selection_sort(data: List[Comparable], descending: bool = False):
    comparator = Comparator(descending)

    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i, len(data)):
            if comparator.less_than(data[j], data[min_idx]):
                min_idx = j
        swap(data, i, min_idx)

    return data