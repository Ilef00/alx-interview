#!/usr/bin/python3

""" Pascal's triangle solution """


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n rows"""
    if n <= 0:
        return []

    # Base cases
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    list_of_lists = pascal_triangle(n - 1)
    last_list = list_of_lists[-1]
    current_list = [1]

    for i in range(len(last_list) - 1):
        current_list.append(last_list[i] + last_list[i + 1])
    current_list.append(1)
    list_of_lists.append(current_list)
    return list_of_lists
