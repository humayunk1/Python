#!/usr/bin/python

"""An implementation of queue in Python 3.5.1
   Code by: Humayun Kabir, humayun.k1@gmail.com"""


class Queue:
    """A Queue implementation"""
    class Node:
        """A linked list node"""
        __slots__ = "_val", "_next"
        def __init__(self, val, n):
            self._val = val
            self._next = n

    def __init__(self):
        """Queue constructor"""
        self._head = None
        self._tail = None
        self._size = 0
        

    def enqueue(self, val):
        """inserts a val in a queue"""
        if self._head is None:
            self._head = self._tail = self.Node(val, self._tail)
            self._size += 1
        else:
            tempNode = self.Node(val, None)
            self._tail._next = tempNode
            self._tail = tempNode
            self._size += 1
            
    def dequeue(self):
        """Deletes a value from the queue"""
        if self._size == 1:
            tempVal = self._head._val
            self._head = None
            self._tail = None
            self._size -= 1
            return tempVal
        else:
            tempVal = self._head._val
            self._head = self._head._next
            self._size -= 1
            return tempVal

    def isEmpty(self):
        """Checks if the queue is empty"""
        return self._head is None

    def __iter__(self):
        temp = self._head
        while temp is not None:
            yield temp._val
            temp = temp._next

    def __str__(self):
        return " ".join(str(i) for i in iter(self))

if __name__ == "__main__":
    que = Queue()

    que.enqueue(10)
    que.enqueue(25)
    que.enqueue(35)

    print( que )

    print("Deleted: ", que.dequeue())
    print( que )
        

