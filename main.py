from gnaoh.sorting import *
from random import randint

def gen_random_list(n: int = 10, low: int = -100, high: int = 100):
    return [randint(low, high) for _ in range(n)]

if __name__ == '__main__':
    l = gen_random_list(n=10)
    # l = bubble_sort(l, descending=True)
    # l = insertion_sort(l)
    # l = selection_sort(l, descending=True)
    # l = merge_sort(l, descending=True)
    # l = quick_sort(l, descending=True)
    l = heap_sort(l, descending=True)

    print(l)