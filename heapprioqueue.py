# priority queue implemented using a min-heap
from prioqueueABC import PrioQueueABC
import numpy as np
import ADTiterator as it
from ADTexceptions import *
from ADTtypemap import typemap
import copy

class HeapPrioQueue(PrioQueueABC):
    """
    Priority Queue implemented using a min-heap
    Attributes
    - _dtype (a class) - type of data values associated with priorities
    default is type(int())
    - _capacity (int) - the size of the min-heap array
    - _last (int) - the last occupied index in the min-heap array
    - _sequenceNo (int) - the next sequence number to assign to an entry
    - _array (numpy 1D array) - an array of Nodes managed as a min-heap
    """
    DEFAULT_CAPACITY = 25
    
    class Node:
        """Nodes in the min-heap"""
        def __init__(self, prio, datum, seqno):
            """
            Construct min-heap node
            Parameters
            - prio - priority for this node
            - datum - value for this node
            - seqno - sequence number for this node
            Effects
            - Node instance ready to be stored in the min-heap
            """
            self._prio = prio
            self._datum = datum
            self._seqno = seqno

    @classmethod
    def duplicatePrioQueue(cls, prioQueue):
        """
        Duplicate an existing PrioQueue
        Used by __iter__ to guarantee the correct ordering of (prio,datum)
        tuples (by priority)
        Parameters
        - prioQueue - the existing priority queue
        Returns
        - deep copy of prioQueue
        """
        newq = copy.deepcopy(prioQueue)
        return newq

    def __init__(self, capacity = DEFAULT_CAPACITY, dtype = type(int())):
        """
        Construct heap-based priority queue ADT
        Parameters
        - capacity (int) - initial capacity for the min-heap, default of 25
        - dtype (class) - element type in the min-heap, default type(int())
        Effects
        - empty prio queue object ready to act line one
        Raises
        - Memory Error if allocation of _array fails
        while all of the other ADT implementation classes delegate setting
        _dtype to the abstract base class, cannot do this here because of the
        shallow copy class method above; thus, directly set _dtype here
        """
        self._dtype = typemap(dtype)
        self._capacity = capacity
        self._last = 0
        self._sequenceNo = 1
        try:
            theType = type(HeapPrioQueue.Node(0,0,0))
            self._array = np.empty(self._capacity, dtype=theType)
        except:
            raise MemoryError('HeapPrioQueue - unable to allocate array')


    def __str__(self):
        """Document metadata about the PrioQueue"""
        return 'HeapPrioQueue - capacity:{}, size:{}, dtype:{}'.format(
            self._capacity, self._last, self._dtype)

    def clear(self):
        """
        Empty the PrioQueue
        Effects
        - after return, isEmpty() invoked on the PrioQueue returns True
        """
        self._last = 0

    def _realCompare_(self, n1, n2):
        """
        Comparison function to guarantee FIFO ordering when prio1 == prio2
        Parameters
        - n1 - a node in the min-heap
        - n2 - another node in the min-heap
        Returns
        - an integer value < 0 if n1._prio < n2._prio
        - an integer value > 0 if n1._prio > n2._prio
        - n1._sequenceNo - n2._sequenceNo if n1._prio == n2._prio
        - note that the function never returns a value of 0
        """
        ans = PrioQueueABC._compare_(n1._prio, n2._prio)
        if ans == 0:
            ans = n1._seqno - n2._seqno
        return ans

    def _siftup_(self):
        """
        Re-establishes heap property of min-heap array
        Effects
        - if heap(1, n-1) is true, and a value is added to index n in the
        array, heap(1, n) will be true upon return
        """
        i = self._last
        while i > 1:
            p = i // 2
            if self._realCompare_(self._array[p], self._array[i]) <= 0:
                break
            tmpnode = self._array[p]
            self._array[p] = self._array[i]
            self._array[i] = tmpnode
            i = p

    def insert(self, prio, datum):
        """
        Insert (prio, datum) into the correct place in the PrioQueue
        Parameters
        - prio - priority for this entry
        - datum - datum associated with this priority in this entry
        Effects
        - (prio,datum) will be inserted into the min-heap array such that
        the array satisfies the heap property
        Raises
        - TypeError if type(datum) is different from _dtype
        - MemoryError if allocation of a larger array fails
        """
        if type(datum) != self._dtype:
            raise TypeError(
                'HeapPrioQueue.insert - type(datum) {} != {}'.format(
                    type(datum), self._dtype
                )
            )
        i = self._last + 1
        if i >= self._capacity:
            new_capacity = 2 * self._capacity
            try:
                theType = type(HeapPrioQueue.Node(0,0,0))
                new_array = np.empty(new_capacity, dtype=theType)
            except:
                raise MemoryError('HeapPrioQueue - unable to allocate array')
            for j in range(1,i):
                new_array[j] = self._array[j]
            self._capacity = new_capacity
            self._array = new_array
        node = HeapPrioQueue.Node(prio, datum, self._sequenceNo)
        self._sequenceNo += 1
        self._last = i
        self._array[i] = node
        self._siftup_()

    def min(self):
        """
        Return (prio,datum) for the highest priority entry in the PrioQueue
        Returns
        - (prio,datum) for the highest priority entry in the PrioQueue
        Raises
        - EmptyError if the PrioQueue is empty
        """
        if self._last == 0:
            raise EmptyError('HeapPrioQueue.min - deque is empty')
        return (self._array[1]._prio, self._array[1]._datum)


    def _siftdown_(self):
        """
        Re-establishes heap property of min-heap array
        Effects
        - if heap(2, n) is true, the the value at index n is moved to
        index 1, heap(1, n-1) will be true upon return
        """
        i = 1
        while True:
            c = 2 * i

            if (c > self._last):
                break
            c2 = c + 1
            if (c2 <= self._last and
                self._realCompare_(self._array[c2], self._array[c]) < 0):
                c = c2
            if self._realCompare_(self._array[i], self._array[c]) <= 0:
                break
            tmpnode = self._array[i]
            self._array[i] = self._array[c]
            self._array[c] = tmpnode
            i = c

    def removeMin(self):
        """
        remove and return (prio,datum) for the highest priority entry in the
        PrioQueue
        Returns
        - (prio,datum) for the highest priority entry in the PrioQueue
        Effects
        - one fewer entries in the PrioQueue
        Raises
        - EmptyError if the PrioQueue is empty
        """

        if self._last == 0:
            raise EmptyError('HeapPrioQueue.removeMin - deque is empty')
        node = self._array[1]
        self._array[1] = self._array[self._last]
        self._last -= 1
        self._siftdown_()
        return (node._prio, node._datum)

    def isEmpty(self):

        """
        Indicate if the PrioQueue is empty
        Returns
        - True if the PrioQueue has no elements
        - False otherwise
        """
        return self._last == 0

    def size(self):
        """
        Return the number of elements in the PrioQueue
        Returns
        - the number of elements in the PrioQueue, >= 0
        """
        return self._last

    def _genArray_(self):
        """
        Generate an array of (prio,value) tuples ordered by priority
        Returns
        - numpy 1D array of (prio,valuie) tuples ordered by priority
        Raises
        - Memory Error if array allocation failure
        """

        pq = HeapPrioQueue.duplicatePrioQueue(self)
        n = pq._last
        try:
            x = np.empty(n, dtype=type(tuple))
        except:
            raise MemoryError(
                'HeapPrioQueue._genArray_ - unable to allocate array'
            )
        j = 0
        for i in range(1, self._last+1):
            node = pq._array[1]
            x[j] = (node._prio, node._datum)
            j += 1
            pq._array[1] = pq._array[pq._last]
            pq._last -= 1
            pq._siftdown_()
        return x

    def toArray(self):
        return self._genArray_()

    def itCreate(self):
        """
        returns iterator over the (prio,datum) elements, in priority order
        Returns
        - Iterator instance
        Raises
        - MemoryError if allocation of array fails
        """
        n = self._last
        x = self._genArray_()
        return it.Iterator(n, x)
