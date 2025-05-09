from abc import ABC, abstractmethod

class DequeABC(ABC):

    """Abstract base class for Deques"""
    @abstractmethod
    def __str__(self):
        """
        Derived class must generate string representation for Deque
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """
        Clear elements from Deque
        Effects
        155156 CHAPTER 9. DEQUES - DOUBLE-ENDED QUEUES
        - Deque is empty
        """
        pass

    @abstractmethod
    def insertFirst(self, datum):
        """
        Insert element at the head of the deque
        Parameters
        - datum - an instance of the data type stored in the Deque
        Effects
        - deque has one additional element, inserted before the
        prior head
        """
        pass
    
    @abstractmethod
    def insertLast(self, datum):
        """
        Insert element at the tail of the deque
        Parameters
        - datum - an instance of the data type stored in the Deque
        Effects
        - deque has one additional element, inserted after the
        prior tail
        """
        pass
    
    @abstractmethod
    def first(self):
        """
        Return the element at the head of the deque
        Returns
        - element at the head of the deque
        Raises
        - EmptyError if the deque was empty
        """
        pass
    
    @abstractmethod
    def last(self):
        """
        Return the element at the tail of the deque
        Returns
        - element at the tail of the deque
        Raises
        - EmptyError if the deque was empty
        """
        pass
    
    @abstractmethod
    def removeFirst(self):
        """
        Remove and return the element at the head of the deque
        Returns
        - element at the head of the deque
        Effects
        - deque has one fewer element
        Raises
        - EmptyError if the deque was empty
        """
        pass
    
    @abstractmethod
    def removeLast(self):
        """
        Remove and return the element at the tail of the deque
        Returns
        - element at the tail of the deque
        Effects
        - deque has one fewer element
        Raises
        - EmptyError if the deque was empty
        """
        pass
    
    @abstractmethod
    def isEmpty(self):
        """
        Indicate if deque is empty
        Returns
        - True if the deque has no elements
        - False otherwise
        """
        pass

    @abstractmethod
    def size(self):
        """
        Return number of elements in the Deque
        Returns
        - integer number of elements, >= 0
        """
        pass
    
    def __len__(self):
        """
        Synonym for DequeABC.size
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
        return iterator instance over the deque ordered head to tail
        """
        pass
    
    def __iter__(self):
        """
        Synonym for DequeABC.itCreate
        """
        return self.itCreate()
