""" Chapter 7. Stack and Queues"""

"""
Stacks support last-in, first-out semantics for inserts and deletes, whereas queues are first-in, first-out.
Stack and Queues are usually building blocks in a solution to a complex problem. As we will soon see, they can also
make for stand-alone problems.

Stacks Bootcamp:

A stack supports two basic operations - push and pop. Elements are added (pushed) and removed (popped) in last-in,
    first-out order, as shown in Figure 8.1. If the stack is empty, pop typically returns null or throws an exception.
    
When the stack is implemented using a linked list these operations have O(1) time complexity. If it is implemented 
    using an array, there is a max number entries it can have - push and pop are still O(1).
    
If the array is dynamically resized, the amortized time for both push and pop is O(1). A stack can support additional
    operations such as peek, which returns the top of the stack without popping it.

The last-in, first-out semantics of a stack make it very useful for creating reverse iterators for sequences which
    are stored in a way that would make it difficult or impossible to step back from a given element. This program
    uses a stack to print the entries of a singly-linked list in reverse order.
    
 
"""

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def print_linked_list_in_reverse(head: ListNode):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())


"""
The time and space complexity are O(n), where n is the number of nodes in the list.
As an alternative, we could form the reverse of the list using Solution 7.2. (Reversing a sublist in a list), iterate
    through the list printing entries, then perform another reverse to recover the list - this would have O(n) time
    and O(1) space complexity.
 
 
* Learn to realize when the stack LIFO property is applicable. Parsing typically benefits from a stack.
* Consider augmenting the basic stack or queue data structure to support additional operations, such as finding
    the maximum element.

Know your stack libraries:
Some questions might ask you to build your own stack class; for others, use the built-in list type.

* s.append(e) pushes an element onto the stack. Not much can go wrong with a call to push.
* s[-1] will retrieve, but does not remove, the element at the top of the stack
* s.pop() will remove and return the element at the top of the stack
* len(s) == 0 tests if the stack is empty
"""



"""
8.1. Implement a stack with max API

Design a stack that includes a max operation, in addition to push and pop. The max method should return the maximum 
    value stored in the stack.
Hint: Use additional storage to track the maximum value.
"""
import collections


class Stack:
    """
    max: O(n), O(1) solution
    """
    def __init__(self):
        self.stack = []
    def pop(self):
        return self.stack.pop()
    def push(self, e):
        return self.stack.append(e)
    def max(self):
        return max(self.stack)


class Stack_book:
    """
    max: O(1), O(n) solution
    """
    ElementsWithCachedMax = collections.namedtuple('ElementWithCachedMax',
                                                   ('element', 'max'))
    def __init__(self) -> None:
        self._element_with_cached_max: List[Stack_book.ElementWithCachedMax] = []
    def empty(self) -> bool:
        return len(self._element_with_cached_max) == 0
    def max(self) -> int:
        return self._element_with_cached_max[-1].max
    def pop(self) -> int:
        return self._element_with_cached_max.pop().element
    def push(self, e: int) -> None:
        self._element_with_cached_max.append(
            self.ElementsWithCachedMax(e,
                                       e if self.empty() else max(e,
                                                                  self.max()))
        )

"""
Queues

A queue supports two basic operations - enqueue and dequeue. (If the queue is empty, dequeue typically returns null or 
    throws an exception). Elements are added (enqueued) and removed (dequeued) in first-in, first-out order. The most
    recently inserted element is referred to as the tail or back element, and the item that was inserted least recently
    is referred to as the head or front element.

A queue can be implemented using a linked list, in which case these operations have O(1) time complexity. The queue API
    often includes other operations, e.g., method that returns the item at the head of the queue without removing it,
    a method that returns the item at the tail of the queue without removing it, etc.

A queue can also be implemented using an array; see Problem 8.7.

A deque, also sometimes called a double-ended queue, is a doubly linked list in which all insertions and deletions are
    from one of the two ends of the list, i.e., at the head or the tail. An insertion to the front is commonly called a
    push, and an insertion to the back is commonly called an inject. A deletion from the front is commonly called a pop,
    a deletion from the back is commonly called an eject.
To sum up:
* Push: + front
* Inject: + back
* Pop: - front
* Eject: - back

Queues boot camp

In the following program, we implement the basic queue API - enqueue and dequeue -as well as a max-method, which returns
    the maximum element stored in the queue. the basic idea is to use composition: add a private field that references 
    a library queue object, and forward existing methods (enqueue and dequeue in this case) to that object.

"""

class Queue:
    def __init__(self) -> None:
        self._data: Deque[int] = collections.deque()
    def enque(self, x: int) -> None:
        self._data.append(x)
    def dequeue(self) -> None:
        self._data.popleft()
    def max(self) -> int:
        return max(self._data)

"""
Queues are ideal when order needs to be preserved.

`
import collections; 
queue_ex = collections.deque()
`
Know your queue libraries:
* q.append(e)
* q[0] will retrieve, but not remove, the element at the front of the queue. q[-1] - same for last element.
* q.popleft() will remove and return the element at the front of the queue.
"""

"""
8.6. Compute binary tree nodes in order of increasing depth

Each node in a binary tree has a depth, which is its distance from the root.

Given a binary tree, return an array consisting of the keys at the same level. Keys should appear in the order of the 
    corresponding nodes' depths, breaking ties from left to right. For example, you should return
    <<314>, <6,6>, <271,561,2,271>, <28,0,3,1,28>, <17,401,257>, <641>> for the binary tree figure 9.1. on pg 118.


	        314                  depth: 0
	    /         \              
	   6           6             depth: 1
	  / \         / \            
	271 561     2    271         depth: 2
   / \    \      \      \        
 28  0    3      1      28       depth: 3
         /      / \              
        17    401  257           depth: 4
                \                
                641              depth: 5

Hint: First think about solving this problem with a pair of queues.
"""

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([
            node.data for node in curr_depth_nodes
        ])
        curr_depth_nodes = [
            child for curr in curr_depth_nodes
            for child in (curr.left, curr.right) if child
        ]
    return result