#!/usr/bin/env python3
"""
Module to perform matrix multiplication.
"""

def mat_mul(mat1, mat2):
    """
    Multiplies two matrices.
    
    Args:
        mat1 (list of list of int/float): The first matrix.
        mat2 (list of list of int/float): The second matrix.
    
    Returns:
        list of list of int/float: The result of the matrix multiplication, or None if matrices cannot be multiplied.
    """
    # Check if matrices can be multiplied
    if len(mat1[0]) != len(mat2):
        return None
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result
