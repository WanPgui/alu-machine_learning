#!/usr/bin/env python3
"""
Module to concatenate two 2D matrices along a specified axis.
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specified axis.
    
    Args:
        mat1 (list of list of int/float): The first matrix.
        mat2 (list of list of int/float): The second matrix.
        axis (int): The axis along which to concatenate (0 for vertical, 1 for horizontal).
    
    Returns:
        list of list of int/float: The concatenated matrix, or None if concatenation is not possible.
    """
    if axis == 0:
        # Check if number of columns is the same
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    
    elif axis == 1:
        # Check if number of rows is the same
        if len(mat1) != len(mat2):
            return None
        return [r1 + r2 for r1, r2 in zip(mat1, mat2)]
    
    else:
        return None
