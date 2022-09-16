from typing import Any, List
from .type import Comparable


class Comparator:
    def __init__(self, descending: bool = False):
        self.descending = descending

    def eq(self, a: Comparable, b: Comparable):
        return a.__eq__(b)

    def less_than(self, a: Comparable, b: Comparable):
        if self.descending:
            return b.__lt__(a)
        else:
            return a.__lt__(b)

    def less_equal(self, a: Comparable, b: Comparable):
        if self.descending:
            return b.__le__(a)
        else:
            return a.__le__(b)

    def greater_than(self, a: Comparable, b: Comparable):
        if self.descending:
            return not b.__le__(a)
        else:
            return not a.__le__(b)

    def greater_equal(self, a: Comparable, b: Comparable):
        if self.descending:
            return not b.__lt__(a)
        else:
            return not a.__lt__(b)

def swap(data: List[Any], i: int, j: int):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

    return data