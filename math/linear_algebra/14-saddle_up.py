#!/usr/bin/env python3
"""
Module to perform matrix multiplication using numpy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication.

    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return np.matmul(mat1, mat2)
