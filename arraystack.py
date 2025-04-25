"""
Copyright (c) 2024, University of Oregon
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
- Neither the name of the University of Oregon nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

from stackABC import StackABC
import numpy as np
import ADTiterator as it
from ADTexceptions import *
from ADTtypemap import typemap
class ArrayStack(StackABC):
    """
    Array-based implementation of the Stack ADT
    Attributes
    - _capacity (int) - default value is 25
    - _dtype - default value is type(int())
    - _next - index into _array for next pushed element
    - _array - numpy 1D array, size _capacity, cells for _dtype elements
    """
    DEFAULT_CAPACITY = 25

    def __init__(self, capacity=DEFAULT_CAPACITY, dtype=type(int())):
        """
        Construct array-based stack
        Parameters
        - capacity (int) - initial capacity for stack, defaults to 25
        - dtype (a class) - type of elements in stack, defaults to type(int())
        Effects
        - object instance ready to act like a stack
        Raises
        - MemoryError - allocation of _array fails
        """

        self._dtype = typemap(dtype)
        self._capacity = capacity
        self._next = 0
        try:
            self._array = np.empty(self._capacity, dtype=self._dtype)
        except:
            raise MemoryError('ArrayStack - unable to allocate array')
        
    def __str__(self):
        """Document metadata about the stack object"""
        return 'ArrayStack - capacity:{}, next:{}, dtype:{}'.format(
            self._capacity, self._next, self._dtype)

    def clear(self):
        """
        Empty the stack
        Effects
        - after return, isEmpty() invoked on the stack returns True
        """
        self._next = 0

    def push(self, datum):
        """
        Push an item on top of the stack; doubles the capacity
        of _array if the stack is full
        Parameters
        - datum - datum of the correct type
        Effects
        - the stack is larger by one element; array has doubled
        in size if upon entry the stack was full
        Raises
        - TypeError - if type of datum is not the same as _dtype
        - MemoryError - if allocation of larger array fails
        """
        if type(datum) != self._dtype:
            raise TypeError(
                'ArrayStack.push - type(datum) {} != {}'.format(
                    type(datum), self._dtype
                )
            )
        if self._next >= self._capacity:
            new_capacity = 2 * self._capacity
            try:
                new_array = np.empty(new_capacity, dtype=self._dtype)
                for i in range(self._capacity):
                    new_array[i] = self._array[i]
                self._capacity = new_capacity
                self._array = new_array
            except:
                raise MemoryError('ArrayStack.push - unable to grow array')
        self._array[self._next] = datum
        self._next += 1

    def peek(self):
        """
        Return element at top of the stack
        Returns
        - top element of the stack
        Raises
        - EmptyError - stack had no elements
        """
        if self._next == 0:
            raise EmptyError('ArrayStack.peek - stack is empty')
        datum = self._array[self._next - 1]
        return datum

    
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
            raise EmptyError('ArrayStack.pop - stack is empty')
        self._next -= 1
        datum = self._array[self._next]
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
    
    def _genArray_(self):
        """
        Helper function to generate array of stack elements
        Returns
        - numpy 1D array ordered top to bottom
        """
        
        n = self._next
        x = self._array[0:n].copy()
        f = 0
        l = n-1
        while f < l:
            t = x[f]
            x[f] = x[l]
            x[l] = t
            f += 1
            l -= 1
        return x
    
    def toArray(self):
        return self._genArray_()
    
    def itCreate(self):
        """
        Returns iterator over stack elements, top to bottom
        Returns
        - Iterator instance
        """
        n = self._next
        x = self._genArray_()
        return it.Iterator(n, x)
