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


def reverse_sublist_book(L: ListNode, s: int, f: int) -> ListNode:
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, s):
        sublist_head = sublist_head.next
    sublist_iter = sublist_head.next
    for _ in range(f - s):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next,
                                                           temp)
    return dummy_head.next
