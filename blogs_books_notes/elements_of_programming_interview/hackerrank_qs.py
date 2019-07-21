""" Qs """


"""
Find unique anagrams.
Given a list of strings, keep the first unique anagrams and delete the rest of the recurring anagrams.
Two strings are anagrams of each other if 
(1) lengths of the string are same
(2) counts of the elements per string are the same.

Return the final list in a sorted order.

"""
from collections import Counter

def uniq_anagrams(input: [str]) -> [str]:
    # O(n log n), O(n)
    counter_list = []
    final_list = []
    for value in input:
        if Counter(value) not in counter_list:  # O(n log (n))
            counter_list.append(Counter(value))  # O(1), O(n)
            final_list.append(value)   # O(1), O(n)
    final_list.sort()  # O(nlog(n))
    return final_list

test_list = ['abcd', 'bcda', 'acbd', 'adbc']

t2 = ['bcda', 'acbd', 'adbc', 'abcd']

t3= ['bcda', 'acbd', 'adbc', 'abcd', 'aabcd', 'abcda', 'baacd', 'bcad']


def _uniq_anagrams(input: [str]) -> [str]:
    counter_list = []
    final_list = []
    def counter(value: str):
        # trying to define the collection's counter myself
        counter_dict = {}
        for x in value:
            try:
                counter_dict[x] += 1
            except KeyError:
                counter_dict[x] = 1
        return counter_dict
    for value in input:
        if counter(value) not in counter_list:
            counter_list.append(counter(value))
            final_list.append(value)
    final_list.sort()
    return final_list


def appx_eq(str1: str, str2: str) -> str:
    """
    Returns 'YES' if str1 and str2 are approximately equivalent.
    Two strings are approximately equivalent if
    (1) lengths of the two string elements are the same
    (2) Character's counts are different by no more than 3
    """
    def counter(value: str) -> dict:
        counter_dict = {}
        for val in value:
            try:
                counter_dict[val] += 1
            except KeyError:
                counter_dict[val] = 0
        return counter_dict
    counter1 = counter(str1)
    counter2 = counter(str2)
    if sum(counter1.values()) != sum(counter2.values()):
        return 'NO'
    for k in counter1.keys():
        try:
            if abs(counter1[k] - counter2[k]) > 3:
                return 'NO'
        except KeyError:
            return 'NO'
    return 'YES'



