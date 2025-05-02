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
from queueABC import QueueABC
import numpy as np
import ADTiterator as it
from ADTexceptions import *
from ADTtypemap import typemap

class ArrayQueue(QueueABC):
    """
    Array-based implemetation of the Queue ADT
    Attributes
    - _capacity (int) - default value is 25
    - _dtype - default value is type(int())
    - _count (int) - number of items in the queue
    - _in (int) - index into _array into which the next enqueue will occur
    - _out (int) - index into _array at which the next front/dequeue will
    occur
    - _array - numpy 1D array, size _capacity, cells for _dtype elements
    """
    DEFAULT_CAPACITY = 25
    def __init__(self, capacity = DEFAULT_CAPACITY, dtype = type(int())):
        """
        Construct array-based queue
        Parameters
        - capacity (int) - initial capacity for the queue, defaults to 25
        - dtype (a class) - type of queue elements, defaults to type(int())
        EffectsA.4. ARRAYQUEUE.PY 257
        - object instance ready to act like a queue
        Raises
        - MemoryError - allocation of _array fails
        """

        self._dtype = typemap(dtype)
        self._capacity = capacity
        self._count = 0
        self._in = 0
        self._out = 0
        try:
            self._array = np.empty(self._capacity, dtype=self._dtype)
        except:
            raise MemoryError('ArrayQueue - unable to allocate array')
        
    def __str__(self):
        """Document metadata about the queue object"""
        st = 'ArrayQueue - capacity:{}, count:{}, next_in: {}'
        st += ', next_out: {}, dtype:{}'
        return st.format(self._capacity, self._count, self._in,
                         self._out, self._dtype)
    def clear(self):
        """
        Empty the queue
        Effects
        - after return, isEmpty() invoked on the queue returns True
        """
        self._count = 0
        self._in = 0
        self._out = 0
        
    def enqueue(self, datum):
        """
        Enqueue an item at the tail of the queue
        Doubles the capacity of _array if the queue is full
        Parameters
        - datum - datum of the correct type
        Effects
        - the queue is larger by one element; array has doubled
        in size if upon entry the queue was full
        Raises
        - TypeError if type of datum is not the same as _dtyhpe
        - MemoryError if allocation of the larger array fails
        """
        
        if type(datum) != self._dtype:
            raise TypeError(
                'ArrayQueue.push - type(datum) {} != {}'.format(
                    type(datum), self._dtype
                )
            )
        
        if self._count >= self._capacity:
            new_capacity = 2 * self._capacity
            try:
                new_array = np.empty(new_capacity, dtype=self._dtype)
                n = self._count
                i = self._out
                j = 0
                while n > 0:
                    new_array[j] = self._array[i]
                    n -= 1
                    j += 1
                    i = (i + 1) % self._capacity
                self._array = new_array
                self._capacity = new_capacity
                self._out = 0
                self._in = self._count    
            except:
                raise MemoryError(
                    'ArrayQueue.enqueue - unable to grow array'
                )
        self._array[self._in] = datum
        self._in = (self._in + 1) % self._capacity
        self._count += 1
            
    def front(self):
        """
        Return element at the head of the queue
        Returns
        - element at the head of the queue
        Raises
        - EmptyError if the queue is empty
        """
        if self._count == 0:
            raise EmptyError('ArrayQueue.front - queue is empty')
        datum = self._array[self._out]
        return datum
    
    def dequeue(self):
        """
        Remove and return element at the head of the queue
        Returns
        - element at the head of the queue
        Effects
        - queue has one fewer elements
        Raises
        - EmptyError if the queue is empty
        """
        if self._count == 0:
            raise EmptyError('ArrayQueue.dequeue - queue is empty')
        datum = self._array[self._out]
        self._count -= 1
        self._out = (self._out + 1) % self._capacity
        return datum

    def isEmpty(self):
        """
        Indicate if queue is empty
        Returns
        - True if queue has no elements
        - False otherwise
        """
        return self._count == 0
    
    def size(self):
        """
        Return the number of elements in the queue
        Returns
        - the number of elements in the queue, >= 0
        """
        return self._count
    
    def _genArray_(self):
        """
        Return numpy 1D array with queue contents
        Returns
        - numpy 1D array with queue contents ordered head to tail
        Raises
        - MemoryError if unable to allocate array
        """

        n = self._count
        try:
            x = np.empty(n, dtype=self._dtype)
        except:
            raise MemoryError('ArrayQueue.__iter__ - unable to allocate array')

        i = self._out
        j = 0
        while n > 0:
            x[j] = self._array[i]
            n -= 1
            j += 1
            i = (i + 1) % self._capacity
        return x

    def toArray(self):
        return self._genArray_()
    
    def itCreate(self):
        """
        Returns iterator over queue elements head to tail
        Returns
        - Iterator instance
        """
        n = self._count
        x = self._genArray_()
        return it.Iterator(n, x)
