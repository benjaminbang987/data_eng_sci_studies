""" Introduction """

"""
Implement h index which refers to the maximum common number of:
(1) # of citations for a published paper
(2) # of cited papers

Example:
a = ['A', 'B', 'C', 'D', 'E', 'F']
b = [4, 1, 3, 2, 3, 1]

ans = 3 (A, C, E have been cited at least 3 times)
"""


def h_index(name_list, cited_list) -> int:
    # naive case O(n^2)
    i = 0
    max_counter = 0
    while i < len(name_list):
        cur_cited_count = cited_list[i]
        j = 0
        cur_cited_count_counter = 0
        while j < len(cited_list) and cur_cited_count != cur_cited_count_counter:
            if cited_list[i] <= cited_list[j]:
                cur_cited_count_counter += 1
            j += 1
        if cur_cited_count <= cur_cited_count_counter and cur_cited_count > max_counter:
            max_counter = cur_cited_count
        elif cur_cited_count > cur_cited_count_counter and cur_cited_count_counter > max_counter:
            max_counter = cur_cited_count_counter
        i += 1
    return max_counter


# improved solution

def h_index_opt(name_list, cited_list):  # O(n log (n))
    cited_list.sort()  # O(nlog(n))
    cur_i = 0
    while cited_list[cur_i] < len(cited_list[cur_i + 1:]): # O(n)
        cur_i += 1
    return cited_list[cur_i]




