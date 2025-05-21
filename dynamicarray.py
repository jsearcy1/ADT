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

from listABC import ListABC
import numpy as np
import ADTiterator as it
from ADTexceptions import *
from ADTtypemap import typemap
import pdb

class DynamicArray(ListABC):
    """
    Array-based version of the List ADT
    Attributes
    - _capacity (int) - current size of _array, defalut is 25
    - _dtype - data type of array elements, default is type(int())
    - _size (int) - number of elements in the list
    - _array - numpy 1D array, size _capacity, cells for _dtype elements
    """
    DEFAULT_CAPACITY = 25
    
    def __init__(self, capacity = DEFAULT_CAPACITY, dtype = type(int())):
        """
        Construct array-based list
        Parameters
        - capacity (int) - initial capacity for the list, default 25
        - dtype (a class) - type of elements in the list, default type(int())
        Effects
        - object instance readdy to act like a list
        Raises
        - MemoryError - allocation of _array fails
        """
        self._dtype = typemap(dtype)
        self._capacity = capacity
        self._size = 0
        try:
            self._array = np.empty(self._capacity, dtype=self._dtype)
        except:
            raise MemoryError('DynamicArray - unable to allocate array')
        
    def __str__(self):
        """Document metadata about the list object"""
        return 'DynamicArray - capacity: {}, size: {}, dtype: {}'.format(
            self._capacity, self._size, self._dtype)
    
    def clear(self):
        """
        Empty the list
        Effects
        - after return, isEmpty() invoked on the list returns True
        """
        self._size = 0
        
    def add(self, datum):
        """
        Append datum to the list
        Parameters
        - datum - instance of the type specified when the list was created
        Effects
        - the list is larger by one element; array has doubled in size if
        upon entry the list was full
        Raises
        - TypeError if the type of datum is not the same as _dtype
        - MemoryError if allocation of a larger array fails
        """
        if typemap(type(datum)) != self._dtype:
            raise TypeError(
                'DynamicArray.add - type(datum) {} != {}'.format(
                    type(datum), self._dtype
                )
            )
        if self._size >= self._capacity:
            new_capacity = 2 * self._capacity
            try:
                new_array = np.empty(new_capacity, dtype=self._dtype)
                for i in range(self._capacity):
                    new_array[i] = self._array[i]
                self._capacity = new_capacity
                self._array = new_array
            except:
                raise MemoryError('DynamicArray.add - unable to grow array')
        self._array[self._size] = datum
        self._size += 1

    def get(self, index):
        """
        Obtain value contained at index in the list250 APPENDIX A. GENERIC IMPLEMENTATIONS
        Parameters
        - index - an index into the array, 0 <= index < _size
        Returns
        - the value at self._array[index]
        Raises
        - IndexError if index < 0 or index >= _size
        """
        if index >= 0 and index < self._size:
            return self._array[index]
        else:
            st = 'DynamicArray.get - illegal index {}'
            raise IndexError(st.format(index))
        
    def isEmpty(self):
        """
        Indicate if the list is empty
        Returns
        - True if the list has no elements
        - False otherwise
        """
        return self._size == 0

    def set(self, index, datum):
        """
        Store a new datum at a particular index
        Parameters
            - index - integer in the range [0,_size)
            - datum - instance of the correct type
        Effects
            - datum now the value stored at index
        Raises
            - TypeError if type mismatch between datum and _dtype
            - IndexError if index < 0 or index >= _size
        """
        if typemap(type(datum)) != self._dtype:
            raise TypeError('DynamicArray.add - type(datum) {} != {}'.format(
                type(datum), self._dtype))
            
        if index < 0 or index >= self._size:
            raise IndexError('DynamicArray.set - bad index {}'.format(index))
        self._array[index] = datum


    def size(self):
        """
        Return the number of elements in the list
        Returns
        - the number of elements in the list, >= 0
        """
        return self._size

    def toArray(self):
        """
        Returns [o,_size] slice of _array.
        """
        return self._array[0:self._size]

    def itCreate(self):
        """
        Returns iterator over list elements in index order
        Returns
        - Iterator instance
        """
        n = self._size
        x = self._array[0:n].copy()
        return it.Iterator(n, x)
        
