#!/usr/bin/env python3
"""function calcuates the integral
of a polynomial
"""


def poly_integral(poly, C=0):
    """polynomial intregral

    Args:
        poly: is list of coefficients representing
        a polynomial where the index of the list
        represents the power of x that the coefficient

    C: is an integer representing the integration constant

    Returns:
        A new list of coefficients for the integral,
        or None if poly or C is not valid
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int):
        return None
    for coef in poly:
        if not isinstance(coef, (int, float)):
            return None

    integral = [C]
    for power in range(len(poly)):
        value = poly[power] / (power + 1)
        if value.is_integer():
            value = int(value)
        integral.append(value)
    return integral
