from typing import Iterable


class NodeList:
    def __init__(self, value, next = None):
        self.value = value

        self.next = next

class LinkedList:
    def __init__(self, values: Iterable = None):
        self.head = None
        self.tail = None

        if values is not None:
            for value in values:
                self.add_last(value)

    def __len__(self):
        iter = self.head
        len = 0

        while iter is not None:
            len += 1
            iter = iter.next

        return len

    def __getitem__(self, idx):
        iter = self._get_node_by_idx(idx)

        return iter.value
    
    def add_first(self, value):
        node = NodeList(value)

        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
        
        self.head = node

    def add_last(self, value):
        node = NodeList(value)

        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node

    def insert(self, value, index: int):
        if index == 0:
            return self.add_first(value)

        iter = self._get_node_by_idx(index - 1)

        node = NodeList(value, iter.next)
        iter.next = node

    def pop_first(self):
        if self.head is None:
            raise ValueError("List is empty")

        val = self.head.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return val

    def pop_last(self):
        if self.head is None:
            raise ValueError("List is empty")

        iter = self.head
        while iter.next is not None:
            iter = iter.next

        val = iter.next.value
        self.tail = iter
        self.tail.next = None

        return val

    def remove(self, index: int):
        if index == 0:
            return self.pop_first()

        # get previous node
        iter = self._get_node_by_idx(index - 1)

        val = iter.next
        # iter at tail
        if iter.next.next is None:
            self.tail = iter
        iter.next = iter.next.next

        return val

    def swap(self, idx1: int, idx2: int):
        if idx1 > idx2:
            self.swap(idx2, idx1) # make sure that idx1 <= idx2
        elif idx1 < idx2:
            prev2 = self._get_node_by_idx(idx2 - 1)
            # case idx1 is head: node1 -> a -> ... -> prev2 -> node2 -> b -> ...
            if idx1 == 0:
                node1 = self.head
                node2 = prev2.next

                prev2.next = node1

                next1 = node1.next
                next2 = node2.next
                node2.next = next1
                node1.next = next2
                self.head = node2 # update head
            else:
                # case: prev1 -> node1 -> next1 -> ... -> prev2 -> node2 -> next2 -> ...
                prev1 = self._get_node_by_idx(idx1 - 1)
                node1 = prev1.next
                node2 = prev2.next

                prev1.next = node2
                prev2.next = node1

                next1 = node1.next
                next2 = node2.next
                node2.next = next1
                node1.next = next2

        self._check_sanity()

    def _get_node_by_idx(self, idx: int) -> NodeList:
        if self.head is None:
            raise ValueError("List is empty")
        elif idx < 0:
            raise ValueError("Index out of range")

        iter = self.head

        while idx > 0 and iter is not None:
            iter = iter.next
            idx -= 1

        if idx > 0:
            raise ValueError("Index out of range")

        return iter 

    def _check_sanity(self):
        if self.head is not None:
            iter = self.head
            while iter.next is not None:
                iter = iter.next
            
            self.tail = iter

    def tolist(self):
        iter = self.head
        out = []

        while iter is not None:
            out.append(iter.value)
            iter = iter.next

        return out