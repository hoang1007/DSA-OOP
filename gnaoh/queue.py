from gnaoh import LinkedList


class Queue:
    def __init__(self):
        self._list = LinkedList()

    def push(self, value):
        self._list.add_last(value)

    def pop(self):
        return self._list.pop_first()

    def tolist(self):
        return self._list.tolist()


class Deque(LinkedList):
    def __init__(self):
        super().__init__()