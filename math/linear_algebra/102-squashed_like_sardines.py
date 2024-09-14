#!/usr/bin/env python3
"""
Squashed Like Sardines
"""

def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Returns None if the matrices cannot be concatenated.
    """
    if axis == 0:
        # Check if the number of columns is the same
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Concatenate rows
        return mat1 + mat2
    
    elif axis == 1:
        # Check if the number of rows is the same
        if len(mat1) != len(mat2):
            return None
        # Concatenate columns
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    
    elif axis == 2:
        # Handling 3D matrices: concatenate along the third axis
        if len(mat1) != len(mat2):
            return None
        if any(len(mat1[i]) != len(mat2[i]) for i in range(len(mat1))):
            return None
        return [[m1 + m2 for m1, m2 in zip(mat1_layer, mat2_layer)]
                for mat1_layer, mat2_layer in zip(mat1, mat2)]
    
    else:
        # Unsupported axis
        return None
