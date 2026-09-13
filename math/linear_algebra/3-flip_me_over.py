#!/usr/bin/env python3
"""Module that returns the transpose of a 2D matrix."""

def matrix_transport(matrix):
    return [list(row) for row in zip(*matrix)]