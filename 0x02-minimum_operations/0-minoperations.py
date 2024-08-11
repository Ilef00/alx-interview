#!/usr/bin/python3

"""
Minimum Operations Solution

This module provides a solution to determine the minimum number of
operations needed to achieve exactly `n` 'H' characters in a file.
The operations allowed are "Copy All" and "Paste". The module includes
two functions:

1. prime_factors(n: int) -> dict[int, int]
   - Computes the prime factorization of a given integer `n`.
   - Returns a dictionary where keys are the prime factors and values
   are their counts.

2. min_operations(n: int) -> int
   - Calculates the minimum number of operations needed to get exactly
   `n` 'H' characters.
   - Uses the results from `prime_factors` to determine the total
   number of operations required.
   - Returns the minimum number of operations or 0 if `n` is less than
   or equal to 1.
"""

from typing import Dict


def prime_factors(n: int) -> Dict[int, int]:
    """
    Computes the prime factorization of a given integer.

    Args:
        n (int): The integer to factorize.

    Returns:
        Dict[int, int]: A dictionary where the keys are prime factors
        of `n` and the values are the counts of those prime factors.

    Examples:
        >>> prime_factors(18)
        {2: 1, 3: 2}
    """
    prime_numbers: Dict[int, int] = {}
    divisor: int = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            if divisor in prime_numbers:
                prime_numbers[divisor] += 1
            else:
                prime_numbers[divisor] = 1
            n //= divisor
        divisor += 1

    if n > 1:
        prime_numbers[n] = 1

    return prime_numbers


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations needed to get
    exactly `n` 'H' characters in the file using only "Copy All"
    and "Paste" operations.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required to achieve
        exactly `n` 'H' characters, or 0 if it is not possible.

    Examples:
        >>> min_operations(1)
        0
        >>> min_operations(2)
        2
        >>> min_operations(3)
        3
        >>> min_operations(4)
        4
        >>> min_operations(18)
        9
    """
    if n <= 1:
        return 0

    factors: Dict[int, int] = prime_factors(n)
    number_of_operations: int = 0

    for factor in factors:
        number_of_operations += factor * factors[factor]

    return number_of_operations
