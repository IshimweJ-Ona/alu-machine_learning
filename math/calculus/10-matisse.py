#!/usr/bin/env python3
"""
Function that calculates the derivative
of a polynomial.
"""

def poly_derivative(poly):
    """
    This function will calculate the polynomial derivative.

    Args:
        poly: is list of coefficients, where index is
        the power of x for that coefficient.

    Returns:
        A new list of coefficients for the derivative,
        [0] if the derivaties is 0m or None if poly is invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for coef in poly:
        if not isinstance(coef, (int, float)):
            return None

    der = []
    for power in range(1, len(poly)):
        der.append(poly[power] * power)

    if len(der) == 0 or all(c == 0 for c in der):
        return [0]
    return der
