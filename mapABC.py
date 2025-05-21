""" BSD header removed to conserve space """
from abc import ABC, abstractmethod

class MapABC(ABC):
    """Abstract base class for Maps"""
    @classmethod
    def _equal_(cls, key1, key2):
        """
        Determine if two keys are equal
        Parameters
        - key1 - first key
        - key2 - second key
        Assumptions
        - key objects support the __eq__ method
        Returns
        - True if key1 == key2
        - False otherwise
        """
        return key1 == key2
    
    @abstractmethod
    def __str__(self):
        """
        Derived class must generate string representation for Map
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear all (key,value) pairs from the Map
        Effects
        - Map is empty
        """
        pass

    @abstractmethod
    def containsKey(self, key):
        """
        Indicates if entry with key is in the Map
        Parameters
        - key - key we are looking for
        Returns
        - True if a (k,v) pair with k == key is in the map
        - False otherwise
        """
        pass
    
    # return value associated with key
    @abstractmethod
    def get(self, key):
        """
        Return value associated with key
        Parameters
        - key - key we are looking for
        Returns
        - value associated with keyin the map12.1. THE MAP ABSTRACT CLASS 201
        Raises
        - KeyError if key is not in the map
        """
        pass
    
    def __getitem__(self, key):
        """
        Synonym for MapABC.get
        """
        return self.get(key)
    
    # store (key, value) pair in the map
    @abstractmethod
    def put(self, key, value):
        """
        Store (key, value) pair into the Map
        Parameters
        - key - key for the entry
        - value - value associated with the key
        Effects
        - (key, value) pair is in the map
        """
        pass
    
    def __setitem__(self, key, value):
        """
        Synonym for MapABC.put
        """
        self.put(key, value)
        
    @abstractmethod
    def putUnique(self, key, value):
        """
        Store (k, v) pair in map iff not containsKey(key)
        Parameters
           - key - key for the entry
           - value - value associated with the key
        Effects
            - (key, value) pair is in the map
        Raises
            - KeyError if key was already represented in the map
        """
        pass
    
    @abstractmethod
    def remove(self, key):
        """
        Remove entry associated with key from the Map
        Parameters
        - key - the key to be removed from the map
        Effects
        - subsequent calls to containsKey(key) will return False
        Raises
        - KeyError if the map did not have an entry for that key
        """
        pass

    @abstractmethod
    def isEmpty(self):
        """
        Indicate if map is empty
        Returns
        - True if the map has no elements
        - False otherwise
        """
        pass
    
    def size(self):
        """
        Return number of (k,v) pairs in the map
        Returns
        - integer number of (k,v) pairs, >= 0
        """
        pass

    def __len__(self):
        """
        Synonym for MapABC.size
        """
        return self.size()
    
    @abstractmethod
    def keyArray(self):
        """
        Return an unsorted array of keys in the Map
        Returns
        - unsorted array of keys in the map
        Raises
        - MemoryError is there was a problem allocating the array
        """
        pass
    
    @abstractmethod
    def toArray(self):
        """
        return unordered numpy 1D array of (key,value) pairs
        """
        pass

    @abstractmethod
    def itCreate(self):
        """
        Return iterator instance over the (key, value) tuples
        the tuples are returned unordered
        """
        pass
    
    def __iter__(self):
        """
        Synonym for MapABC.itCreate
        """

        return self.itCreate()
