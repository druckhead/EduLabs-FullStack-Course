from __future__ import annotations
from copy import deepcopy
from functools import singledispatchmethod
from types import NoneType
from typing import Any, Self


class Node:
    @singledispatchmethod
    def __init__(self, value=None) -> None:
        return NotImplemented

    def __str__(self) -> str:
        str = "<Node: "
        if self._prev is not None:
            str += f"prev = {self._prev._value}"
        else:
            str += f"prev = {None}"
        str += f" val = {self._value} "
        if self._next is not None:
            str += f"next = {self._next._value}"
        else:
            str += f"next = {None}"
        str += ">"

        return str

    def __repr__(self) -> str:
        return f"<Node: val={self._value}>"

    @__init__.register(int)
    @__init__.register(float)
    @__init__.register(str)
    def _from_value(self, value):
        self._value: Any = value
        self._next: Self = None
        self._prev: Self = None


@Node.__init__.register(Node)
def _from_node(self, node):
    self._value: Any = node._value
    if node._prev is not None:
        self._prev: Self = Node(node._prev._value)
    else:
        self._prev: Self | None = None
    if node._next is not None:
        self._next: Self = Node(node._next._value)
    else:
        self._next: Self | None = None


class LinkedList:
    def __init__(self, other_iterable=None) -> None:
        if other_iterable is None:
            self._len = 0
            self._head: Node | None = None
            self._tail: Node | None = None
        elif isinstance(other_iterable, LinkedList):
            self._len = other_iterable._len
            self._head: Node = deepcopy(other_iterable._head)
            p = self._head
            while p._next is not None:
                p = p._next
            self._tail = p
        else:
            raise NotImplemented()

    @property
    def len(self):
        return self._len

    def append(self, value):
        if self._len == 0:
            self._head = Node(value)
            self._tail = self._head
        else:
            new_node = Node(value)
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = self._tail._next
        self._len += 1

    def insert_at(self, value, index):
        if index > self._len:
            raise IndexError("linked list index out of range")
        new_node = Node(value)
        if index == 0:
            self._head._prev = new_node
            new_node._next = self._head
            self._head = new_node
        else:
            curr_ind = 0
            p = self._head
            while p._next is not None and curr_ind < index - 1:
                p = p._next
                curr_ind += 1
            new_node._prev = p
            new_node._next = p._next
            p._next = new_node
        self._len += 1

    def remove_from(self, index):
        if index > self._len:
            raise IndexError("linked list index out of range")
        curr_ind = 0
        p = self._head
        while p._next is not None and curr_ind < self._len:
            p = p._next
            curr_ind += 1
        p._next = p._next._next

    def __add__(self, other: Self):
        new_ll = LinkedList(self)
        other_list = LinkedList(other)
        
        p = other._head
        while p is not None:
            new_ll.append(p._value)
            p = p._next
        
        return new_ll


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(55)
    ll.append(22)
    ll.append(33)
    ll.insert_at(77, 2)
    ll.insert_at(69, 2)
    ll.insert_at(420, 0)

    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(6)
    ll2.append(7)
    ll2.append(8)

    ll3 = ll + ll2
    print(ll3)
