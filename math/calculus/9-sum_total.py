#!/usr/bin/env python3
"""Function calculating the sum of squares"""


def summation_i_squared(n):
    """
    Calculates the sum of i^2 from i = 1 to n
    
    Args:
        n: the stopping condition, must be a positive integer

    Returns:
        The integer value of the sum, or None if n is not valid
    """
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
