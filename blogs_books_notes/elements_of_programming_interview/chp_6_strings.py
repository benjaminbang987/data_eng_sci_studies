""" Chapter 6. Strings """

"""
Bootcamp:

palindromic string - reads the same when it's reversed.
"""


def is_palindromic(s: str) -> bool:
    # s[~i] for i in [0, len(s) - 1] is s[-(i+1)]
    # O(n) and O(1)
    return all(s[i] == s[~i] for i in range(len(s) // 2))


"""
Bootcamp:

Know your string libraries:

The key operators and functions on strings are s[3], len(s), s+t s[2:4], s in t, s.strip(), s.startswith(prefix),
    s.endswith(suffix), 'Euclid,Axiom 5,Parallel Lines'.split(','), 3 *'01',
    ','.join(('Benjamin', 'Bang', 'ASA'))
    s.tolower(), 'Name {name}, Rank {rank}'.format(name='Benjamin', rank=3),
    chr and ord
    
* strings are immutable: operations like s = s[1:] or s+= '123' imply creating a new array of characters that is then
    assigned back to s. This implies that concatenating a string character n times to a string in a for loop has 
    O(n^2) times complexity.
* Simple put, a mutable object can be changed after it is created, and an immutable object can’t. Objects of built-in 
    types like (int, float, bool, str, tuple, unicode) are immutable. Objects of built-in types like (list, set, dict)
    are mutable.
"""

"""
6.1 Interconvert strings and integers

A string may encode an integer, e.g., "123" encodes 123. In this problem you are to implement methods that take a string 
    representing an integer and return the corresponding integer, and vice versa. Your code should handle negative
    values. You cannot use library functions like int in Python. 

Implement an integer to string conversion function and a string to integer conversion function. For example, if the 
    input to the first function is the integer 314, it should return the string "314", and if the input to the second
    function is the string "314", it should return integer 314.
    
Hint: Build the result one digit at a time.
"""


def int_to_str(int_obj: int) -> str:
    # O(n^2)
    # O(n^2)
    i = 1
    s = ""
    while int_obj != int_obj % i + i:
        i *= 10
    while int_obj > 0:
        s = s + "{val}".format(val=int_obj // i)
        int_obj = int_obj % i
        i = round(i / 10)
    return s

import functools
import string


def int_to_str_book(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


def str_to_int(s: str) -> int:
    """
    '1234'

    """
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


"""
6.2 Base Conversion

Write a program that performs base conversion. The input is a string, an integer b1, and another integer b2. The string
    represents an integer in base b1. The output should be the string representing the integer in base b2. Assume
    2 <= b1, b2, <=16. Use "A" to represent 10, "B" for 11, ... and "F" for 15.

Hexdigits - 1, 2, 3, 4, .. 8, 9, a, b, c, d, e, f, A, B, C, D, E, F
    
Ex:
"615", b1 = 7, b2 = 13. Result "1A7"
(6 * 7 ** 2 + 1 * 7 + 5 = 1 * 13 ** 2 + 10 * 13 + 7  = 306)
"""
import string


# fail
def base_cv(bstr, b1, b2):
    # brute force
    running_sum = 0
    string_len = len(bstr) - 1
    for b in bstr:
        running_sum = string.digits.index(b) * b1 ** string_len + running_sum
        string_len -= 1
    def max_p(num, base):
        p1 = 0
        while base ** (p1 + 1) < num and p1 <= 15:
            p1 += 1
        return num - base ** (p1), p1
    power_list = []
    while running_sum > 0:
        running_sum, p1 = max_p(running_sum, b2)
        power_list.append(chr(ord('0') + p1))
    num_dict = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }
    for i in range(len(power_list)):
        try:
            power_list[i] = num_dict[power_list[i]]
        except KeyError:
            pass
    return ''.join(power_list)


# after hint: use modulo
def base_cv2(bstr, b1, b2):
    # doesn't account for negative strings..
    running_sum = 0
    string_len = len(bstr) - 1
    for b in bstr:
        running_sum = string.digits.index(b) * b1 ** string_len + running_sum
        string_len -= 1
    list_b2 = []
    num_dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    while running_sum > 0:
        running_sum, p2 = running_sum // b2, running_sum % b2
        try:
            list_b2.append(num_dict[p2])
        except KeyError:
            list_b2.append(chr(ord('0') + p2))
    return ''.join(reversed(list_b2))


# book solution
def base_cv_book(bstr, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())
    is_neg = bstr[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        bstr[is_neg:],
        0)
    return ('-' if is_neg else '') + ('0' if num_as_int == 0 else
                                      construct_from_base(num_as_int, b2))


"""
6.3 Replace and Remove

Write a program which takes as input an array of characters and removes each 'b' and replaces each 'a' by two 'd's.
    Specifically, along with the array, you are provided an integer-valued size. Size denotes the number of entries
    of the array that the operation is to be applied to. You do not have to worry about preserving subsequent entries.
    For example, if the array is <a, b, a, c, >, and the size is 4, then you can return <d, d, d, d, c>. You can assume
    there is enough space in the array to hold the final result.

Hint: consider performing multiple passes on s.
 
"""

test_list = ['a', 'b', 'a', 'c', None]
test_list_2 = ['a', 'a', 'b', 'c', 'b', 'c']
def rep_and_rem(size: int, array_of_strings: [str]) -> [str]:
    # first loop to remove 'b'
    # second loop to replace ['a'] with ['d', 'd']
    # O(n), O(n)
    # this is wrong, since it's not altering the input array
    new_list = []
    for val in array_of_strings[:size]:
        if val == 'a':
            new_list.append('d')
            new_list.append('d')
        elif val != 'b':
            new_list.append(val)
    return new_list


def rep_and_rem_book(size: int, array_of_strings: [str]) -> int:
    """book solution - reproduced after reading the solution"""
    write_idx, a_count = 0, 0
    for i in range(size):
        if array_of_strings[i] != 'b':
            array_of_strings[write_idx] = array_of_strings[i]
            write_idx += 1
        if array_of_strings[i] == 'a':
            a_count += 1
    #
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    #
    while cur_idx >= 0:
        if array_of_strings[cur_idx] == 'a':
            array_of_strings[write_idx - 1: write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            array_of_strings[write_idx] = array_of_strings[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size
