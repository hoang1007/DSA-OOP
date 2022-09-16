from typing import List
from .type import Comparable
from .functional import Comparator

def merge_sort(data: List[Comparable], descending: bool = False):
    comparator = Comparator(descending)

    return merge_recursive(data, 0, len(data) - 1, comparator)


def merge_recursive(data: List[Comparable], low: int, high: int, comparator: Comparator):
    if low == high:
        return [data[low]]

    mid = (low + high) // 2

    left_vals = merge_recursive(data, low, mid, comparator)
    right_vals = merge_recursive(data, mid + 1, high, comparator)

    merged_vals = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_vals) and right_idx < len(right_vals):
        if comparator.less_than(left_vals[left_idx], right_vals[right_idx]):
            merged_vals.append(left_vals[left_idx])
            left_idx += 1
        else:
            merged_vals.append(right_vals[right_idx])
            right_idx += 1

    while left_idx < len(left_vals):
        merged_vals.append(left_vals[left_idx])
        left_idx += 1

    while right_idx < len(right_vals):
        merged_vals.append(right_vals[right_idx])
        right_idx += 1

    del left_vals
    del right_vals
    return merged_vals