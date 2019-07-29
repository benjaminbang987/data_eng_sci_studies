""" Chapter 7. Linked Lists"""

"""
Bootcamp:


Tips:
* Very often, a problem on lists is conceptually simple, and is more about cleanly coding what's specified, rather than
    designing an algorithm.
* Consider using a dummy head (sometimes referred to as a sentinel) to avoid having to check for empty lists. This
    simplifies code, and makes bugs less likely.
* It's easy to forget to update next (and previous for double linked list) for the head and tail.
* Algorithms operating on singly linked lists often benefit from using two iterators, one ahead of the other, or one
    advancing quicker than the other.

"""

"""
# 7.1 Merge two sorted linked lists.

Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field your program can
    change in a node is its next field.

Hint
"""


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# failed solution - 20 minutes
def merge_sorted_lls(l1: ListNode, l2: ListNode) -> ListNode:
    cur_l1 = l1
    cur_l2 = l2
    def traverse_and_add(cur_l1, cur_l2):
        l1_next = cur_l1.next
        l2_next = cur_l2.next
        cur_l1.next = cur_l2
        cur_l2.next = l1_next
        cur_l1 = l1_next
        cur_l2 = l2_next
    while cur_l1.data or cur_l2.data:
        if cur_l2.next is None:
            if cur_l2.data > cur_l1.data and cur_l2.data < cur_l1.next.data:
                traverse_and_add(cur_l1, cur_l2)
        elif cur_l1.next is None:
            if cur_l1.data > cur_l2.data and cur_l1.data < cur_l2.next.data:
                traverse_and_add(cur_l2, cur_l1)
        else:
            if cur_l2.data > cur_l1.data and cur_l2.data < cur_l1.next.data:
                traverse_and_add(cur_l1, cur_l2)
            elif cur_l1.data > cur_l2.data and cur_l1.data < cur_l2.next.data:
                traverse_and_add(cur_l2, cur_l1)


# test sets

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6, ListNode(11, ))))))
l2 = ListNode(4, ListNode(10))


def merge_sorted_lls_retry(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = tail = ListNode()
    while l1 and l2:
        if l1.data < l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy_head.next


def ll_to_list(l1: ListNode):
    return_list = []
    while l1:
        return_list.append(l1.data)
        l1 = l1.next
    return return_list

l3 = merge_sorted_lls_retry(l1, l2)
ll_to_list(l3)
# [1, 2, 3, 4, 5, 6, 10, 11]

"""
7.2. Reverse a Single Sublist

Write a program which takes a singly linked list L and two integers s and f as arguments, and reverses the order of the
    nodes from the s-th node to f–th node, inclusive. The numbering begins at 1, i.e., the head node is the first node.
    Do not allocate additional nodes.

# Hint: Focus on the successor fields which have to be updated.
"""

# 20 mins and fail
def reverse_sublist(L: ListNode, s: int, f: int) -> ListNode:
    dummy_head = cur = ListNode(0, L)
    for _ in range(1, s):
        cur = cur.next

    sublist_iter = cur.next
    for _ in range(f - s):
        temp = cur.next
        sublist_iter.next,

    while s > 1:
        cur.data = l1.data
        cur, l1 = cur.next, l1.next
        s -= 1
    while f > 1:

        , l1 = ,l1.next
        f -= 1


    cur.next = another_dummy
    return dummy_head.next


# [1, 2, 3, 4, 5, 6, 10, 11]
def reverse_sublist_kev(L: ListNode, s: int, f: int) -> ListNode:
    dummy_head = dummy = ListNode(0, L)
    start = None
    for i in range(f):
        if i == s - 1:
            start = dummy
        dummy = dummy.next
    post = dummy.next
    prev = dummy
    temp = start.next
    for _ in range(f - s + 1):
        temp = temp.next
        start.next, prev = prev, temp
        start = start.next
    start.next = post
    return dummy_head.next


# retry (7/28/2019)
def reverse_sublist(L: ListNode, s: int, f: int) -> ListNode:
    head_dummy = head_pointer = ListNode(0, L)
    for _ in range(1, s):
        head_pointer = head_pointer.next
    head_iter = head_pointer.next
    for _ in range(0, f - s):
        temp = head_iter.next
        head_pointer.next, temp.next, head_iter.next = (
            temp,
            head_pointer.next,
            temp.next
        )
    return head_dummy.next

# test
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, )))))))
l3 = reverse_sublist(l1, 3, 6)
ll_to_list(l3)


"""
7.2. Test for Cyclicity
Although a linked list is supposed to be a sequence of nodes ending in null, it is possible to create a cycle in a
    linked list by making the next field of an element reference to one of the earlier nodes.

Write a program that takes the head of a singly linked list and returns null if there does not exist a cycle, and the
    node at the start of the cycle, if a cycle is present. (You do not know the length of the list in advance).

Hint: Consider using two iterators, one fast and one slow.
"""


def is_cycle(L: ListNode):
    """
    Q: Can you have duplicate values in nodes?
    A: Yes

    O(n * log n), O(n)
    This solution is actually wrong - it's not returning the start of the cycle - it's just returning the start of the
        whole list.
    """
    dummy_head = pointer = ListNode(0, L)
    pointer_list = []
    while pointer.next and pointer.next not in pointer_list:
        pointer_list.append(pointer)
        pointer = pointer.next
    if pointer.next is None:
        return
    else:
        return dummy_head.next


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, )))))))
l1.next.next.next.next.next.next.next = l1.next.next.next # linking ListNode(7,) with ListNode(4, ...)


def is_cycle_book_my_try(L: ListNode):
    """
    O(n) and O(1)
    fast iterator and slow iterator.
    1. Figure out whether there is a cycle
    2. If there is a cycle, figure out the cycle length (C)
    3. Figure out the node where the cycle begins
    """
    def calc_cycle_len(end):
        start, steps = end, 0
        while True:
            steps += 1
            start = start.next
            if start == end:
                break
        return steps
    slow_node = fast_node = L
    while fast_node and fast_node.next and fast_node.next.next:
        slow_node, fast_node = slow_node.next, fast_node.next.next
        if slow_node is fast_node:
            back_node = front_node = L
            for _ in range(calc_cycle_len(slow_node)):
                front_node = front_node.next
            while back_node is not front_node:
                back_node, front_node = back_node.next, front_node.next
            return back_node
    return


l3 = is_cycle_book_my_try(l1)




