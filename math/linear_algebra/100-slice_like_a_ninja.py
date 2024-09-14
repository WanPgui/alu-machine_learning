#!/usr/bin/env python3
"""
Demonstrate numpy slicing along specified axes.
"""

import numpy as np

def np_slice(matrix, axes={}):
    """
    Slice a NumPy matrix along specified axes.

    Args:
        matrix (np.ndarray): The matrix to slice.
        axes (dict): A dictionary where the key is an axis to slice along
                     and the value is a tuple representing the slice
                     to make along that axis.

    Returns:
        np.ndarray: The sliced matrix.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("The matrix must be a numpy.ndarray.")
    
    if not isinstance(axes, dict):
        raise TypeError("Axes must be a dictionary.")
    
    # Create a list of slices for each dimension
    slices = [slice(None)] * matrix.ndim
    
    for ax, slice_spec in axes.items():
        if ax < 0 or ax >= matrix.ndim:
            raise ValueError(f"Axis {ax} is out of bounds for matrix with {matrix.ndim} dimensions.")
        if not isinstance(slice_spec, tuple):
            raise TypeError("Each slice specification must be a tuple.")
        slices[ax] = slice(*slice_spec)
    
    return matrix[tuple(slices)]
