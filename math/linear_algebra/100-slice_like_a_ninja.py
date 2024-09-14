#!/usr/bin/env python3
import numpy as np

def np_slice(matrix, axes={}):
    # Create a tuple for slicing, with default slicing of ':' for each axis
    slices = tuple(axes.get(i, slice(None)) for i in range(matrix.ndim))
    return matrix[slices]
