#!/usr/bin/env python3
"""
Module to slice a matrix along specific axes using numpy.
"""

import numpy as np


def np_slice(matrix, axes={}):
    """
    Slices a matrix along specified axes.

    Args:
        matrix (numpy.ndarray): The matrix to slice.
        axes (dict): A dictionary where keys are axes and values are slices.

    Returns:
        numpy.ndarray: The sliced matrix.
    """
    slices = [slice(None)] * matrix.ndim
    for axis, slice_tuple in axes.items():
        slices[axis] = slice(*slice_tuple)

    return matrix[tuple(slices)]
