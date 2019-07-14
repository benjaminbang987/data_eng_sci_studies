""" Chapter 2. Arrays """

"""
Get, set: O(1)
Insert: O(n)
Delete: O(n)
"""


"""
Array bootcamp problem:
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
"""


def even_odd(A: [int]) -> None:
    # Time, space: O(n), O(1)
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


"""
General advice:
Array problems often have simple brute-force solutions in O(n) space, but there are subtler solutions that use
    the array itself to reduce space complexity to O(1).

Filling an array from the front is slow, so see if it's possible to write values from the back.

Instead of deleting an entry, consider overwriting it. 

When dealing with integers encoded by an array, consider processing the digits from the back of the array. 
    Alternatively, reverse the array so the least-significant digit is the first entry.

Be comfortable with writing code that operates on subarrays.

It's incredibly easy to make off-by-1 errors when operating on arrays - reading past the last element of an array
    is a common error which has catastrophic consequences.
    
Don't worry about preserving the integrity of the array (sortedness, keeping entries together, etc) until it is time to
    return.

When operating on 2D arrays, use parallel logic for rows and for columns.  
"""

"""
Know your array libraries:
Arrays in Python are provided by the `list` type. (The `tuple` type is very similar to the `list` type, with the 
    constraint that it is immutable). `List` is dynamically-resized.
    
Syntax example:
    [3, 5, 7, 1] + [0] * 10, list(range(100))

Basic operations:
    len(A), A.append(3), A.remove(3) and A.insert(i, x)
    a in A (returns True if a is in A list, False otherwise): O(n)
    

Understand the difference between
    B = A
    B = list(A)

Understand what a deep copy vs shallow copy is (copy.copy(A) vs copy.deepcopy(A)).

Key methods:
    min(A), max(A)
    bisect.bisect(A, 6), bisect.bisect_left(A, 6), bisect.bisect_right(A, 6) (for binary search - import bisect)
    A.reverse() (in-place), reversed(A) (returns an iterator), A.sort() (in-place), sorted(A) (returns a copy), 
    del A[i] (deletes the i-th element), del A[i:j] (removes the slice)

Slicing:

e.g. 2D arrays:
    [[1, 2, 4], [3, 5, 7, 9], [13]]
"""

"""
# problem 5.1: Dutch National Flag Problem

Write a program that takes an array A and an index i into A, and rearranges the elements such that all elements
    less than A[i] (the "pivot") appear first, followed by elements equal to the pivot, followed by elements greater
    than the pivot.
"""
# test case
A = [0, 1, 2, 0, 2, 1, 1]


def partition(A: [], i: int) -> None:
    # naive case
    # Speed: O(n)
    # Space: O(2 * n) = O(n)
    a, b, c = [], [], []
    for num in A:
        if num < A[i]:
            a.append(num)
        elif num == A[i]:
            b.append(num)
        elif num > A[i]:
            c.append(num)
    return a + b + c


def partition_opt(A: [], i: int) -> None:
    # optimized for space
    # Speed: O(n)
    # Space: O(1)
    pivot = A[i]
    smaller, bigger = 0, len(A) - 1
    for j in range(len(A)):
        if A[j] < pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller += 1
    for j in reversed(range(len(A))):
        if A[j] > pivot:
            A[j], A[bigger] = A[bigger], A[j]
            bigger -= 1


def dutch_flag_partition(A: [], pivot_index: int) -> None:
    # (this was what I was trying to do, but it seems like I needed an additional 'equal' index
    # also optimized
    # Speed: O(n)
    # Space: O(1)
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


"""
5.6 Buy and sell stock once
 

"""



