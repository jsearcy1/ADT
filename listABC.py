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

from abc import ABC, abstractmethod

class ListABC(ABC):
    """Abstract base class for Lists"""
    @abstractmethod
    
    def __str__(self):
        """
        Derived class must generate string representation for List
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear elements from List
        Effects
        - List is empty
        """
        pass
    
    # add element to end of the list
    @abstractmethod
    def add(self, datum):
        """
        Add element to the end of the list
        Parameters
        - datum - an instance of the data type stored in the List
        Effects
        """
        pass
    
    @abstractmethod
    def get(self, index):
        """
        - List has one more element, with datum at the highest index
        Return element at index in the list
        Parameters
        - index - an integer in the range [0,size)
        Returns
        - returns the element stored at that index
        Raises
        - IndexError if index < 0 or index >= size
        """
        pass
    

    def __getitem__(self, index):
        """
        Synonym for ListABC.get
        """
        return self.get(index)
    
    @abstractmethod
    def isEmpty(self):
        """
        Indicate if the list is empty
        Returns
        - True if the list has no elements
        - False otherwise
        """
        return self._size == 0

    @abstractmethod
    def set(self, index, datum):
        """
        Store datum at index
        Parameters
        - index - an integer in the range [0,size)88 CHAPTER 4. ABSTRACT DATA TYPES
        - datum - an instance of the data type stored in the List
        Effects
        - datum is stored at index
        Raises
        - IndexError if index < 0 or index >= size
        """
        pass
    

    def __setitem__(self, index, datum):
        """
        Synonym for ListABC.set
        """
        self.set(index, datum)
        
    @abstractmethod    
    def size(self):
        """
        Return number of elements in the list
        Returns
        - integer number of elements, >= 0
        """
        pass

    def __len__(self):
        """
        Synonym for ListABC.size
        """
        return self.size()
    
    @abstractmethod
    def toArray(self):
        """
        return numpy 1D array of elements ordered by index
        """
        pass

    @abstractmethod
    def itCreate(self):
        """
        Return iterator instance over the list, ordered by index
        from 0 to size-1
        """
        pass
    
    def __iter__(self):
        """
        Synonym for ListABC.itCreate
        """
        return self.itCreate() 
