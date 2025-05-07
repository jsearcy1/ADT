from stackABC import StackABC
import numpy as np
import ADTiterator as it
from ADTexceptions import *
from ADTtypemap import typemap

class LListStack(StackABC):
    class Node:
        """ Node in the singly-linked list """
        def __init__(self, datum):
            self._datum = datum
            self._next = None
            
    def __init__(self, dtype = type(int())):
        """
        Construct llist-based stack

        Parameters
        - dtype (a class) - type of stack elements, defaults to type(int())
        
        Effects
        - object instance ready to act like a stack
        """
        self._dtype = typemap(dtype)
        self._count = 0
        self._head = None
        
    def __str__(self):
        """Document metadata about the stack object"""
        return 'LListStack - count:{}, dtype:{}'.format(
                self._count, self._dtype)

    def clear(self):
        """
        Empty the stack

        Effects
          - after return, isEmpty() invoked on the stack returns True
        """
        self._count = 0
        self._head = None


    def push(self, datum):
        the_type = typemap(type(datum))
        if the_type != self._dtype:
            raise TypeError(
                'LListStack.push - type(datum) {} != {}'.format(
                    the_type, self._dtype
                )
            )
        node = self.Node(datum)
        node._next = self._head
        self._head = node
        self._count += 1
        
    def peek(self):
        if self._count == 0:
            raise EmptyError('LListStack.peek - stack is empty')
        return self._head._datum

    def pop(self):
        if self._count == 0:
            raise EmptyError('LListStack.pop - stack is empty')
        node = self._head
        datum = node._datum
        self._head = node._next
        self._count -= 1
        return datum
    
    def isEmpty(self):
        return self._count == 0

    def size(self):
        return self._count
 
    def _genArray_(self):
        n = self._count
        try:
            x = np.empty(n, dtype=self._dtype)
        except:
            raise MemoryError('LListStack._genArray_ - unable to allocate array')
        p = self._head
        j = 0
        while p != None:
            x[j] = p._datum
            p = p._next
            j += 1
        return x
    
    def toArray(self):
        return self._genArray_()

    def itCreate(self):
        n = self._count
        x = self._genArray_()
        return it.Iterator(n, x)


if __name__ == "__main__":
 
    
    # Test Code
    pass
