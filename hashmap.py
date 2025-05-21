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
from mapABC import MapABC
import numpy as np
import ADTiterator as it
from ADTexceptions import *
from ADTtypemap import typemap

class HashMap(MapABC):
    """
    Hash-based implementation of the Map ADT
    Attributes
    - _dtype (class) - type of data associated with keys
    - _size (int) - number of entries in the Map
    - _hash (function) - applied to a key yields an integer
    - _capacity (int) - number of hash buckets
    - _changes (int) - number of changes in entries since last resize check
    - _load (float) - current load (entries/buckets)
    - _loadFactor (float) - target load
    - _increment (float) - change in load with each put or remove
    - _buckets (numpy 1D array) - hash buckets
    """
    DEFAULT_CAPACITY = 16
    DEFAULT_LOAD_FACTOR = 0.75
    MAX_CAPACITY = 134217728
    TRIGGER = 100
    class Entry:
        """key/value object"""
        def __init__(self, key, value):
            """
            Constructor for entry
            Parameters
            - key - the key to be associated with this entry
            - value - the value to be associated with this key
            Effects
            - object instance ready to act like an Entry
            """
            self._key = key
            self._value = value
            
    class Node:
        """Node for bucket linked lists"""
        def __init__(self, entry):
            """
            Constructor for node in hash table
            Parameters
            - entry - an instance of HashMap.Entry
            Effects
            - Node ready for insertion into a bucket list
            """
            self._next = None
            self._mentry = entry
            
    def __init__(self, hashfxn = hash, dtype = type(int()),
                 capacity = DEFAULT_CAPACITY,
                 loadFactor = DEFAULT_LOAD_FACTOR):
        """
        Constructor for Hash-based Map
        Parameters
        - hashfxn: function that hashes key to yield an int
        - dtype: type of data in the map, default type(int())
        - capacity: initial number of buckets, default DEFAULT_CAPACITY
        - loadFactor: target load factor, default DEFAULT_LOAD_FACTOR
        Effects
        - object instance ready to act like a map
        Raises
        - MemoryError if allocation of _buckets fails
        """
        self._dtype = typemap(dtype)
        self._size = 0
        self._hash = hashfxn
        self._capacity = capacity
        if capacity > HashMap.MAX_CAPACITY:
            self._capacity = HashMap.MAX_CAPACITY
        self._changes = 0
        self._load = 0.0
        self._loadFactor = loadFactor
        if loadFactor < 0.001:
            self._loadFactor = HashMap.DEFAULT_LOAD_FACTOR
        self._increment = 1.0 / self._capacity
        n = self._capacity
        try:
            x = np.empty(n, dtype=type(HashMap.Node))
        except:
            raise MemoryError('HashMap - unable to allocate bucket array')

        for i in range(n):
            x[i] = None
        self._buckets = x
        
    def __str__(self):
        """Document metadata about the map object"""
        return 'HashMap - buckets: {}, size:{}, dtype:{}'.format(
            self._capacity, self._size, self._dtype)
    
    def clear(self):
        """
        Empty the map
        Effects
        - after return, isEmpty() invoked on the map returns True
        """
        self._size = 0
        self._load = 0.0
        self._changes = 0
        for i in range(self._capacity):
            self._buckets[i] = None

    def _findKey_(self, key):
        """
        Find the entry associated with a particular key
        Parameters
        - key - the key in which we are interested
        Returns
        - (bucketIndex, Node)
        + bucketIndex the index into _buckets to which the key hashes
        + Node - the node in that bucket which matched key OR None
        """
        bi = self._hash(key) % self._capacity
        node = self._buckets[bi]
        while node != None:
            if MapABC._equal_(key, node._key):
                break
            node = node._next
        return (bi, node)
    
    def containsKey(self, key):
        """
        Indicate whether the key is resident in the map
        Parameters
        - key - the key in which we are interested
        Returns
        - True if an entry with key is in the Map
        - False otherwise
        """
        return self._findKey_(key)[1] != None

    def get(self, key):
        """
        Return value associated with key
        Parameters
        - key - the key in which we are interested
        Returns
        - value associated with key
        Raises
        - KeyError if containsKey(key) == False
        """
        node = self._findKey_(key)[1]
        if node == None:
            raise KeyError('HashMap.get - invalid key')
        return node._value
    
    def _insertNewEntry_(self, key, value, bi):
        """
        Insert a new entry into the map
        Parameters
        - key - key associated with entry
        - value - value associated with key
        - bi - bucket index to which key hashes to
        Effects
        - entry for (key, value) added to map
        - one more entry in the map
        Raises
        - TypeError if type(value) not equal to _dtype
        - This code assumes the caller has guaranteed that an entry with
        key does not already exist in themap
        """
        if type(value) != self._dtype:
            raise TypeError(
                'HashMap.put - type(datum) {} != {}'.format(
                    type(datum), self._dtype
                )
            )
        node = HashMap.Entry(key, value)
        node._next = self._buckets[bi]
        self._buckets[bi] = node
        self._size += 1
        self._load += self._increment
        self._changes += 1
        
    def put(self, key, value):
        """
        Store (key,value) into the map
        Parameters
        - key - the key for this entry
        - value - the value to be associated with this key
        Effects
        - if containsKey(key) is True, the value associated with it will be
        replaced by the value parameter
        - if not, (key,value) will be added to the map, and the map will
        be larger by one more entry
        Raises
        - TypeError if type(value) is not equal to _dtype
        """

        if type(value) != self._dtype:
            raise TypeError(
                'HashMap.put - type(value) {} != {}'.format(
                    type(datum), self._dtype
                )
            )
        bi, node = self._findKey_(key)
        if node != None:
            node._value = value
        else:
            self._insertNewEntry_(key, value, bi)

    def putUnique(self, key, value):
        """
        Store (key,value) into the map iff key not already in map
        Parameters
        - key - the key for this entry
        - value - the value to be associated with this key
        Effects
        - (key,value) will be added to the map, and the map will
        be larger by one more entry
        Raises
        - KeyError if there is already an entry using key
        - TypeError if type(value) is not equal to _dtype
        """
        bi, node = self._findKey_(key)
        if node == None:
            self._insertNewEntry_(key, value, bi)
        else:
            raise KeyError('HashMap,putUnique - key already exists')
        
    def remove(self, key):
        """
        Remove the entry associated with key
        Parameters
        - key - the key in which we are interested
        Effects
        - entry associated with key removed from the map
        - there is one fewer entry in the map
        Raises
        - KeyError if containsKey(key) == False
        """
        
        bi, node = self._findKey_(key)
        if node == None:
            raise KeyError('HashMap,remove - key does not exist')
        p = None
        q = self._buckets[bi]
        while q != node:
            p = q
            q = p._next
            if p == None:
                self._buckets[bi] = q._next
            else:
                p._mext = q._next
        self._size -= 1
        self._load -= self._increment
        self._changes += 1
        
    def isEmpty(self):
        """
        Indicate if the map is empty
        Returns
        - True if the map has no entries
        - False otherwise
        """
        return self._size == 0
    
    def size(self):
        """
        Return the number of entries in the map
        Returns
        - the number of entries in the map, >= 0
        """
        return self._size
    
    def keyArray(self):
        """
        Return an array of the keys in the map
        Returns
        - an unordered numpy 1D array of keys in the map
        Raises
        - MemoryError if allocation of the array fails
        """

        n = self._size
        try:
            x = np.empty(n, dtype=object)
        except:
            raise MemoryError('HashMap.keyArray - unable to allocate array')
        i = 0
        j = 0
            
        while i < self._capacity:
            node = self._buckets[i]
            
            while node != None:
                x[j] = node._key
                j += 1
                node = node._next
            i += 1
        return x

    def _genArray_(self):
        """
        Return an unordered array of (key,value) tuples
        Returns
        - numpy 1D array of (key,value) tuples
        Raises
        - MemoryError if array allocation fails
        """

        n = self._size
        try:
            x = np.empty(n, dtype=type(tuple))
        except:
            raise MemoryError('HashMap.__iter__ - unable to allocate array')
        i = 0
        j = 0
        while i < self._capacity:
            node = self._buckets[i]
            while node != None:
                x[j] = (node._key, node._value)
                j += 1
                node = node._next
                i += 1
        return x
    
    def toArray(self):
        return self._genArray_()
    
    def itCreate(self):
        """
        Return in unordered iterator over the map entries
        Returns
        - Iterator instance
        Raises
        - MemoryError if allocation of the array of entries fails
        """

        n = self._size
        x = self._genArray_()
        return it.Iterator(n, x)
