#!/usr/bin/python

"""An implementation of Stack in Python 3.5.1
   Code by: Humayun Kabir, humayun.k1@gmail.com"""


class Stack:
    """A Stack implementation"""
    class Node:
        """A linked list node"""
        __slots__ = "_val", "_next"
        def __init__(self, val, n):
            self._val = val
            self._next = n

    def __init__(self):
        """Stack constructor"""
        self._head = None

    def push(self, val):
        """Pushes a val onto the stack"""
        self._head = self.Node(val, self._head)

    def pop(self):
        """Pops a value off the stack"""
        tempVal = self._head._val
        self._head = self._head._next
        return tempVal

    def isEmpty(self):
        """Checks if the stack is empty"""
        return self._head is None

    def __iter__(self):
        temp = self._head
        while temp is not None:
            yield temp._val
            temp = temp._next

    def __str__(self):
        return " ".join(str(i) for i in iter(self))

if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(30)
    stack.push(40)

    print( stack )

    print("poped: ", stack.pop())
    print( stack )
        

