from abc import ABC, abstractmethod

class PrioQueueABC(ABC):
    """Abstract base class for PrioQueues"""
    # implementations assume that the priority objects support __lt__() and
    # __gt__()

    @classmethod
    def _compare_(cls, oLeft, oRight):
        """
        Ternary compare function
        Parameters
        - oLeft - a priority object
        - oRight - another priority object
        Assumptions
        - priority objects support __lt__() and __gt__()
        Returns
        - -1 if oLeft < oRight
        - 0 if oLeft == oRight
        - +1 if oLeft > oRight
        """
        if oLeft < oRight:
            ans = -1
        elif oLeft > oRight:
            ans = 1
        else:
            ans = 0
        return ans
    
    @abstractmethod
    def __str__(self):
        """
        Derived class must generate string string representation for PrioQueue
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear elements from PrioQueue
        Effects
        - PrioQueue is empty
        """
        pass

    @abstractmethod
    def insert(self, prio, datum):
        """
        Insert element into PrioQueue
        Parameters
        - prio - an instance of a priority object
        - datum - an instance of the data type stored in the PrioQueue
        Effects
        - priority queue has one more element
        - it was inserted according to the total ordering of priorities
        """
        pass
    
    @abstractmethod
    def min(self):
        """
        Return highest priority (prio, datum) pair
        Returns
        - (prio, datum) tuple for the highest priority element
        Raises
        - EmptyError if the priority queue was empty
        """
        pass

    @abstractmethod
    def removeMin(self):
        """
        Remove and return highest priority (prio, datum) pair
        Returns
        - (prio, datum) tuple for the highest priority element
        Effects
        - priority queue has one fewer element
        Raises
        - EmptyError if the priority queue was empty
        """
        pass

    @abstractmethod
    def isEmpty(self):
        """
        Indicate if PrioQueue is empty
        Returns
        - True if the priority queue has no elements
        - False otherwise
        """
        pass
    
    @abstractmethod
    def size(self):
        """
        Return number of elements in the PrioQueue
        Returns
        - integer number of elements, >= 0
        """
        pass
    
    def __len__(self):
        """
        Synonym for PrioQueueABC.size
        """
        return self.size()
    
    @abstractmethod
    def toArray(self):
        """
        return numpy 1D array of elements ordered head to tail
        """
        pass
    
    @abstractmethod
    def itCreate(self) -> "iterator OR MemoryError":
        """
        Return iterator instance over the PrioQueue ordered by priority
        """
        pass
    
    def __iter__(self):
        """
        Synonym for PrioQueueABC.itCreate
        """
        return self.itCreate()
