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

class QueueABC(ABC):
    """Abstract base class for Queues"""
    @abstractmethod
    def __str__(self):
        """
        Derived class must generate string representation for Queue
        """
        pass
    
    @abstractmethod
    def clear(self):
        """
        Clear elements from Queue
        Effects
        - Queue is empty
        """
        pass
    
    @abstractmethod
    def enqueue(self, datum):
        """
        Enqueue element at the tail of the Queue
        Parameters
        - datum - an instance of the data type stored in the Queue
        - Queue has one more element, with datum now being at the tail
        """
        pass
    
    @abstractmethod
    def front(self):
        """
        Return element at the head of the Queue
        Returns
        - element at the head of the queue
        Raises
        - Empty Error if the queue was empty
        """
        pass

    @abstractmethod
    def dequeue(self):
        """
        Remove and return element at the head of the Queue
        Returns
        - element at the head of the queue
        Effects
        - queue has one fewer element
        Raises
        - EmptyError if the queue was empty
        """
        pass
    
    @abstractmethod
    def isEmpty(self):
        """
        Indicate if the Queue is empty
        Returns
        - True if the queue has no elements
        - False otherwise
        """
        pass

    @abstractmethod
    def size(self):
        """
        Return number of elements in the Queue
        Returns
        - integer number of elements, >= 07.2. A GENERIC QUEUE 141
        """
        pass
    
    def __len__(self):
        """
        Synonym for QueueABC.size
        """
        return self.size()
    
    @abstractmethod
    def toArray(self):
        """
        return numpy 1D array of elements ordered head to tail
        """
        pass
    
    @abstractmethod
    def itCreate(self):
        """
        return iterator instance over the Queue ordered head to tail
        """
        pass
    
    def __iter__(self):
        """
        Synonym for QueueABC.itCreate
        """
        return self.itCreate()
