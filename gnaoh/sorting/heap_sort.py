from typing import List
from .type import Comparable
from .functional import swap, Comparator


def heap_sort(data: List[Comparator], descending: bool = False):
    comparator = Comparator(descending)

    # build max heap
    for i in range(len(data) // 2 - 1, -1, - 1):
        data = heapify(data, len(data), i, comparator)

    for i in range(len(data) - 1, 0, -1):
        # swap the largest value to the last, and reduce tree nodes step by step
        swap(data, 0, i)
        data = heapify(data, i, 0, comparator)

    return data

def heapify(data: List[Comparator], len_: int, node_idx: int, comparator: Comparator):
    left_idx = 2 * node_idx + 1
    right_idx = 2 * node_idx + 2

    max_node_idx = node_idx

    if left_idx < len_ and comparator.less_than(data[left_idx], data[max_node_idx]):
        max_node_idx = left_idx

    if right_idx < len_ and comparator.less_than(data[right_idx], data[max_node_idx]):
        max_node_idx = right_idx

    if max_node_idx != node_idx:
        swap(data, max_node_idx, node_idx)
        data = heapify(data, len_, max_node_idx, comparator) # rebuild heap from swapped node

    return data