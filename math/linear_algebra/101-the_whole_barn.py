#!/usr/bin/env python3
"""
Module to add two matrices.
"""

def add_matrices(mat1, mat2):
    """
    Adds two matrices element-wise.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.

    Returns:
        list: The resulting matrix after addition, or None if shapes do not match.
    """
    if len(mat1) != len(mat2):
        return None

    result = []
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
        result.append([x + y for x, y in zip(row1, row2)])
    
    return result
