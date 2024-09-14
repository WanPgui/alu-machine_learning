#!/usr/bin/env python3
"""
Module to concatenate two matrices along a specific axis.
"""

def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specified axis.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.
        axis (int, optional): The axis along which to concatenate. Default is 0.

    Returns:
        list: The concatenated matrix, or None if shapes are not compatible.
    """
    import numpy as np

    np_mat1 = np.array(mat1)
    np_mat2 = np.array(mat2)

    try:
        return np.concatenate((np_mat1, np_mat2), axis=axis).tolist()
    except ValueError:
        return None

