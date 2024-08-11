#!/usr/bin/python3


"""
Minimum Operations Solution

This module provides a solution to determine the minimum number
of operations needed to achieve exactly `n` 'H' characters in a file.
The operations allowed are "Copy All" and "Paste".
The module includes two functions:

1. prime_factors(n: int) -> dict[int, int]
   - Computes the prime factorization of a given integer `n`.
   - Returns a dictionary where keys are the prime factors and values
   are the counts of those factors.

2. minOperations(n: int) -> int
   - Calculates the minimum number of operations needed to get exactly
   `n` 'H' characters.
   - Uses the results from `prime_factors` to determine the total
   number of operations required.
   - Returns the minimum number of operations or 0 if `n` is less than
   or equal to 1.
"""


def prime_factors(n: int) -> dict[int, int]:
    """
    Computes the prime factorization of a given integer.
    Args:
        n (int): The integer to factorize.
    Returns:
        dict[int, int]: A dictionary where the keys are
        prime factors of n and the values are the counts
        of those prime factors.
    """

    prime_numbers: dict[int, int] = {}

    for i in range(2, n + 1):
        while n % i == 0:
            if i in prime_numbers:
                prime_numbers[i] += 1
            else:
                prime_numbers[i] = 1
            n //= i

    return prime_numbers


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to get
    exactly `n` H characters in the file using only "Copy All"
    and "Paste" operations.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required to achieve
        exactly `n` H characters, or 0 if it is not possible.
    """

    if n <= 1:
        return 0

    factors: dict[int, int] = prime_factors(n)
    number_of_operations: int = 0

    for i in factors:
        number_of_operations += i * factors[i]

    return number_of_operations
