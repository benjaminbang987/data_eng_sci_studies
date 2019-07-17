""" Chapter 1. Primitive Types """

"""
Python has a number of built-in types: numerics (e.g. integer), sequence(e.g. list), mappings(e.g. dict), as well as 
  classes, instances and exceptions. All instances of these types are objects.
"""

"""
Yeonhoo's advice: 
잘하는 사람: does well in crossing out the things that won't work (data structures, algorithms, etc)

picks up the hints well (i.e. - try something O(n log n) -> usually refers to solutions with O(n) that's possible - then focus on eliminating O(log n)) ).
If the solution becomes too complicated, then mostly it's not the answer.




"""

# is number palindromic
import collections
import math


def ispalindromic(x: int) -> bool:
    """
    Returns true if the integer is the same forwards/backwards
    121 True
    11 True
    1234321 True
    """
    if x <= 0:
        return False

    num_digits = math.floor(math.log10(x))
    curr_pointer = 10 ** (num_digits)
    for i in range((num_digits + 1) // 2):
        if x % 10 != x // curr_pointer:
            return False
        x = x % curr_pointer
        x = x //10
        curr_pointer = curr_pointer // 100
    return True


class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, left_top: Coordinates, right_bottom: Coordinates):
        self.left_top = left_top
        self.right_bottom = right_bottom


"""
4.1 Computing the Parity of a word
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For example, 1011 has
    parity of 1, and 10001000 has 0.
 
How would you compute the parity of a very large number of 64-bit words?

"""


def partiy(x: int) -> int:
    # Naive
    # Time: O(n)
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


"""
4.11 Rectangle Intersection
Write a program which tests if two rectangles have a nonempty intersection. If the intersection is nonempty,
        return the rectangle formed by their intersection.

    For simplicity, Say x and y coordinates are for left-bottom most point in a Rect namedtuple object.

    Hint: Think of the X and Y dimensions independently.

    Clarifying question: if boundaries touch, does that count as intersecting?
        Answer: Let's say yes for now

"""


def rect_intersection(first_rect: Rect,
                      second_rect: Rect) -> Rect:
    # tests overlap
    # returns Rect of overlap boundaries
    # base case: time O(1), space O(1)
    if second_rect.x > first_rect.x + first_rect.width or first_rect.x > second_rect.x + second_rect.width:
        return Rect(0, 0, -1, -1)
    elif second_rect.y > first_rect.y + first_rect.height or first_rect.y > second_rect.y + second_rect.height:
        return Rect(0, 0, -1, -1)
    else:
        return Rect(max(first_rect.x, second_rect.x), max(first_rect.y, second_rect.y),
                    min(first_rect.x + first_rect.width - second_rect.y,
                        second_rect.x + second_rect.width - first_rect.x),
                    min(first_rect.y + first_rect.height - second_rect.y,
                        second_rect.y + second_rect.height - first_rect.y))


def rect_intersect_book(first_rect: Rect,
                        second_rect: Rect) -> Rect:
    """
    book solution
    """
    def is_intersect(r1, r2):
        return (r1.x <= r2.x + r2.width and r1.y <= r2.y + r2.height
                and r1.x + r1.width >= r2.x and r1.y + r1.height >= r2.y)

    if not is_intersect(first_rect, second_rect):
        return Rect(0, 0, -1, -1)
    return Rect(
        max(first_rect.x, second_rect.x), max(first_rect.y, second_rect.y),
        min(first_rect.x + first_rect.width, second_rect.x + second_rect.width) - max(second_rect.x,first_rect.x),
        min(first_rect.y + first_rect.height, second_rect.y + second_rect.height) - max(second_rect.y, first_rect.y)
    )


Point = collections.namedtuple('Point', ('x', 'y'))


# variant 1
def is_rect(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    # when edges are aligned with X and Y axes
    sorted_x = [p1.x, p2.x, p3.x, p4.x].sort()  # O(n log n)
    sorted_y = [p1.x, p2.x, p3.x, p4.x].sort()  # O(n log n)
    return sorted_x[0] == sorted_x[1] and sorted_x[2] == sorted_x[3]\
           and sorted_y[0] == sorted_y[1] and sorted_y[2] == sorted_y[3]


# variant 1 optimized - if not aligned with X and Y axes

def is_rect_opt(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    # when edges are aligned with X and Y axes
    def get_dist(p1: Point, p2: Point) -> float:
        return ((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)) ** (0.5)
    # O(n)
    dist = set()
    for p_1 in [p1, p2]:
        for p_2 in [p1, p2, p3, p4]:
            if p_1 != p_2:
                dist.add(get_dist(p_1, p_2))
    return len(dist) == 3


# test points
p1 = Point(0,0)
p2 = Point(4, 3)
p3 = Point(-3, 4)
p4 = Point(-1, 7)



