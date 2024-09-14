#!/usr/bin/env python3
"""
Module to calculate the shape of a matrix.
"""


def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list of integers.
    
    Args:
        matrix (list): The matrix for which the shape is calculated.

    Returns:
        list: The shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
