#!/usr/bin/env python3


"""
Module to calculate the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.
    
    Args:
        matrix (list of list): The 2D matrix to transpose.
    
    Returns:
        list of list: The transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]
