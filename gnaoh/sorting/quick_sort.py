from typing import List
from .type import Comparable
from .functional import Comparator, swap

def quick_sort(data: List[Comparable], descending: bool = False):
    comparator = Comparator(descending)

    return quick_sort_recursive(data, 0, len(data) - 1, comparator)


def quick_sort_recursive(data: List[Comparable], low: int, high: int, comparator: Comparator):
    if low < high:
        data, pivot_idx = partition(data, low, high, comparator)

        data = quick_sort_recursive(data, low, pivot_idx - 1, comparator)
        data = quick_sort_recursive(data, pivot_idx + 1, high, comparator)

    return data


def partition(data: List[Comparable], low: int, high: int, comparator: Comparator):
    if low > high:
        raise IndexError

    low_ = low
    high_ = high - 1
    pivot = data[high]

    while True:
        while low_ <= high_ and comparator.less_than(data[low_], pivot):
            low_ += 1

        while low_ <= high_ and comparator.greater_than(data[high_], pivot):
            high_ -= 1

        if low_ >= high_:
            break
        
        swap(data, low_, high_)
        low_ += 1
        high_ -= 1

    swap(data, low_, high) # swap low + 1 (th) value and the pivot

    return data, low_