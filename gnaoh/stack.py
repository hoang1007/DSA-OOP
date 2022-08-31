from gnaoh import LinkedList

class Stack:
    def __init__(self):
        self._list = LinkedList()

    def push(self, value):
        self._list.add_first(value)

    def pop(self):
        return self._list.pop_first()

    def __len__(self):
        return len(self._list)

    def tolist(self):
        return self._list.tolist()