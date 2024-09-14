#!/usr/bin/env python3
"""
Module to add two 2D matrices element-wise.
"""

def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.
    
    Args:
        mat1 (list of lists of int/float): The first matrix.
        mat2 (list of lists of int/float): The second matrix.
    
    Returns:
        list of lists of int/float: The element-wise sum of the two matrices, or None if the matrices are not the same shape.
    """
    # Check if matrices are of the same shape
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None
    
    # Perform element-wise addition
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]
