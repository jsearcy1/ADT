from boundedstackintABC import BoundedStackIntABC
import numpy as np
from ADTexceptions import *

class BoundedArrayStackInt(BoundedStackIntABC):
    """
    Array-based implementation of a bounded integer Stack
    Attributes
    - _capacity (int) - default value is 25
    - _next - index into _array for next pushed element
    - _dtype - the type of elements, np.int64
    - _array - numpy 1D array, size _capacity, cells for int elements
    """
    DEFAULT_CAPACITY = 25


    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        Construct bounded, array-based stack of integers
        Parameters
        - capacity (int) - capacity for stack, defaults to 25
        Effects
        - object instance ready to act like a stack
        Raises
        - MemoryError - allocation of _array fails
        """

        self._dtype = np.dtype(np.int64)
        self._capacity = capacity
        self._next = 0
        try:
            self._array = np.empty(self._capacity, dtype=np.int64)
        except:
            raise MemoryError('BoundedArrayStackInt - array allocation fail')

    def clear(self):
        """
        Empty the stack
        Effects
        - after return, isEmpty() invoked on the stack returns True
        """
        self._next = 0



    def push(self, datum):
        """
        Push an item on top of the stack
        Parameters
        - datum - integer to push onto stack
        Effects
        - the stack is larger by one element
        Raises
        - TypeError - if type of datum is not int
        - FullError - if stack is full
        """
        if type(datum) != self._dtype:
            raise TypeError(
                'BoundedArrayStackInt.push - type(datum) {} != {}'.format(
                    type(datum), self._dtype
                )
            )
        
        if self._next >= self._capacity:
            raise FullError(
                'BoundedArrayStackInt.push - stack is full'
            )
        else:
            self._array[self._next] = datum
            self._next += 1

    def pop(self):
        """
        Remove and return element at top of the stack
        Returns
        - top element of the stack
        Effects
        - stack has one fewer element
        Raises
        - EmptyError - stack had no elements
        """
        if self._next == 0:
            raise EmptyError('BoundedArrayStackInt.pop - stack is empty')
        self._next -= 1
        datum = self._array[self._next]
        return datum


    def peek(self):
        """
        Return element at top of the stack
        Returns
        - top element of the stack
        Raises
        - EmptyError - stack had no elements
        """
        if self._next == 0:
            raise EmptyError('BoundedArrayStackInt.peek - stack is empty')
        datum = self._array[self._next - 1]
        return datum  


    def isEmpty(self):
        """
        Indicate if stack is empty
        Returns
        - True if stack has no elements
        - False otherwise
        """
        return self._next == 0

    def size(self):
        """
        Return the number of elements on the stack
        Returns
        - the number of elements on the stack, >= 0
        """
        return self._next
    
