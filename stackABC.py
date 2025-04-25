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

class StackABC(ABC):
    """Abstract base class for Stacks"""

    @abstractmethod
    def __str__(self):
        """
        Derived class must generate string representation for Stack
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear elements from Stack
        Effects
        - Stack is empty
        """
        pass

    @abstractmethod
    def push(self, datum):
        """
        Push element onto top of the Stack
        Parameters
        - datum - an instance of the data type stored in the Stack
        Effects
        - Stack has one more element, with datum now being on top
        """
        pass
    

    @abstractmethod
    def peek(self):
        """
        Return element at top of the stack
        Returns
        - element at top of the stack
        Raises
        - EmptyError if the stack was empty
        """
        pass
    
    @abstractmethod
    def pop(self):
        """
        Remove and return element at top of the stack
        Returns
        - element at top of the stack
        Effects
        - stack has one fewer element
        Raises
        - EmptyError if the stack was empty
        """
        pass

    @abstractmethod
    def isEmpty(self):
        """
        Indicate if stack is empty
        Returns
        - True if the stack has no elements
        - False otherwise
        """
        pass
    
    @abstractmethod
    def size(self):
        """
        Return number of elements on the stack
        Returns
        - integer number of elements, >= 0
        """
        pass

    def __len__(self):
        """
        Synonym for StackABC.size
        """
        return self.size()
    
    @abstractmethod
    def toArray(self):
        """
        return numpy 1D array of elements ordered top to bottom
        """
        pass

    @abstractmethod
    def itCreate(self):
        """
        Return iterator instance over the stack, top to bottom
        """
        pass
    
    def __iter__(self):
        """ 
        Synonym for StackABC.itCreate
        """
        return self.itCreate()
