import numpy as np
from dynamicarray import DynamicArray
from arraystack import ArrayStack
from boundedarraystackint import  BoundedArrayStackInt 
from arrayqueue import ArrayQueue
from lliststack import LListStack


def test_dynamic_array_capacity():
    dynarr=DynamicArray(capacity=1)
    [dynarr.add(0) for i in range(4)]
    assert dynarr._capacity==4

def test_dynamic_array_add():
    dynarr=DynamicArray(capacity=1)
    [dynarr.add(i) for i in range(4)]
    assert (dynarr.toArray()==np.array([0,1,2,3])).all()

def test_dynamic_array_memerr():
    try:
        DynamicArray(capacity=int(1e13))
    except Exception as e:
        assert type(e)==MemoryError
        

def test_arraystack_toarray():
    stack=ArrayStack()
    [stack.push(i) for i in range(3)]
    print(stack.toArray())
    assert (stack.toArray()==np.array([2,1,0])).all()

def test_arraystack_pop():
    stack=ArrayStack()
    [stack.push(i) for i in range(3)]    
    assert [stack.pop() for i in range(3)]==[2,1,0]

def test_arraystack_iter():
    stack=ArrayStack()
    [stack.push(i) for i in range(3)]    
    assert [i for i in stack]==[2,1,0]

    
def test_boundedarraystackint_pop():
    stack=BoundedArrayStackInt()
    [stack.push(i) for i in range(3)]    
    assert [stack.pop() for i in range(3)]==[2,1,0]

def test_arrayqueue():
    queue=ArrayQueue()
    [queue.enqueue(i) for i in range(3)]    
    assert [queue.dequeue() for i in range(3)]==[0,1,2]

def test_llstack_push():
   new_stack=LListStack()
   new_stack.push(26)
   assert new_stack._count == 1


def test_llstack_dtype_exception():
   new_stack=LListStack(dtype=float)
   exc=None
   try:
       new_stack.push(int(26))
   except Exception as e:
       exc=e
       pass

   assert not (exc is None)

