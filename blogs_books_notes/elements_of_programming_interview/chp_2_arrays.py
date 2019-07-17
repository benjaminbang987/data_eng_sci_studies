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
 
Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be made 
    by buying and then selling one share of that stock. There is no need to buy if no profit is possible.

Hint: Identifying the minimum and maximum is not enough since the minimum may appear after the maximum height.
    Focus on valid differences.
"""

test_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def max_profit(prices: [float]) -> float:
    """
    Q: Can the stock price be negative?
    A: No

    """
    # naive solution
    # Speed: O(n)
    # Space: O(n)
    buy = prices[0]
    cur_sum = 0
    profits = []
    for price in prices:
        if price >= buy:
            cur_sum += price - buy
        else:
            profits.append(cur_sum)
            cur_sum = 0
        buy = price
    profits.append(cur_sum)
    return max(profits)


def max_profit_ben_opt(prices: [float]) -> float:
    """
    Optimize it s.t. space complexity is O(1)
    """
    buy = prices[0]
    cur_sum = 0
    max_pro = 0
    for price in prices:
        if price >= buy:
            cur_sum += price - buy
        else:
            if cur_sum > max_pro:
                max_pro = cur_sum
            cur_sum = 0
        buy = price
    return max_pro


def max_profit_book_opt(prices: [float]) -> float:
    """
    Optimize it s.t. space complexity is O(1)
    """
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

"""
5.6 variant:
Write a program that takes an array of integers and finds the length of a longest subarray all of whose entries are 
    equal. 
"""


def len_longest_same_int(ints: [int]) -> int:
    """
    O(n), O(1)
    """
    max_length, cur_length = 0, 0
    prev = ints[0]
    for integer in ints:
        if integer == prev:
            cur_length += 1
            max_length = max(max_length, cur_length)
        else:
            prev = integer
            cur_length = 1
    return max_length


"""
5.12 Sample Offline Data

Implement an algorithm that takes as input an array of distinct elements and a size, and returns a subset of the given 
    size of the array elements. All subsets should be equally likely. Return the result in input array itself.
    
Hint: How would you construct a random subset of size k + 1 given a random subset of size k?
"""

import random


def _sample(users: [int], k: int) -> None:
    """
    * Need to update the input array instead of creating a new one.

    """

    for i in range(k):
        r_i = random.randint(i, len(users) - 1)
        users[r_i], users[i] = users[i], users[r_i]


"""
5.18 Compute the spiral ordering of a 2D array

Write a program which takes an n x n 2D array and returns the spiral ordering of the array.

Hint: Use case analysis and divide-and-conquer
"""

array_2d_3v3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_2d_4v4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def spiral_order(square_matrix: [[int]]) -> [int]:
    """
    Returns the spiral ordered elements of the square matrix.
    """
    # get first and last row. For in between rows, only get first and last element
    # create list of first + last elements of middle rows + reversed last row + first elements of middle rows
    # pop the elements and call the function again on the leftover 2d array

    # ben's first failed attempt:
    # reason: too complicated traverse_spiral function
    spiral_values = []

    def traverse_spiral(sub_square_matrix: [[int]]):
        if len(sub_square_matrix) == 1:
            spiral_values.append(sub_square_matrix[0])
        n = len(sub_square_matrix) - 2  # index of items that we need per row/column
        spiral_values.append(sub_square_matrix[0][:n])  # O(n)
        for row in sub_square_matrix:
            spiral_values.append(row.pop())
        spiral_values.append(sub_square_matrix[n + 1][::-1])  # O(n)
        sub_square_matrix = sub_square_matrix[1:n]  # O(n)
        new_n = len(sub_square_matrix) - 1
        while new_n > 0:
            spiral_values.append(sub_square_matrix[new_n][0])
            sub_square_matrix[new_n] = sub_square_matrix[new_n][1:]  # O(n)
            new_n -= 1

        # some sort of operations to redefine the square matrix
        # some operation to add values to spiral_values
        # recursive call on the leftover matrix
        traverse_spiral(sub_square_matrix)

    traverse_spiral(square_matrix)
    return spiral_values


def spiral_order_book_sol1(square_matrix: [[int]]) -> [int]:
    """
    Returns the spiral ordered elements of the square matrix (book solution 1)

    <tip> list(zip(*rows)) gives converts lists with rows into lists with columns & vice versa.

    The * character is known as the unpacking operator. when it appears behind an iterable object, what it does is
        passing the items inside the iterable to the function's caller one by one. In this case, since the zip function
        accepts a list of iterables in order to return their aligned columns, zip(*p) passes all the items inside the
        p as arguments to zip function:
    """
    # O(n^2)
    spiral_values = []
    def traverse_clockwise(offset: int):
        if offset == len(square_matrix) - offset - 1:
            # boundary condition. This condition passes if offset >= (len(square_matrix)-1)/2
            spiral_values.append(square_matrix[offset][offset])
            return
        spiral_values.extend(
            square_matrix[offset][offset:- 1 - offset]
        )  # first row elements
        spiral_values.extend(
            list(zip(*square_matrix))[- 1 - offset][offset:- 1 - offset]
        )  # last column elements
        spiral_values.extend(
            square_matrix[-offset - 1][-1 - offset:offset:-1]
        )  # last row elements
        spiral_values.extend(
            list(zip(*square_matrix))[offset][- 1 - offset: offset: -1]
        )  # first column elements
    for offset in range((len(square_matrix) + 1) // 2):
        traverse_clockwise(offset)
    return spiral_values


def spiral_order_book_sol2(square_matrix: [[int]]) -> [int]:
    """
    Returns the spiral ordered elements of the square matrix (book solution 2)

    Try solving this using while loop and two pointers to the end (col_end and row_end):
    col_start = row_start = 0
    row_end = len(matrix) - 1
    col_end = len(matrix[0]) - 1
    """
