#!/usr/bin/env python3
"""
Module to add two arrays element-wise.
"""

def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.
    
    Args:
        arr1 (list of int/float): The first array.
        arr2 (list of int/float): The second array.
    
    Returns:
        list of int/float: The element-wise sum of the two arrays, or None if the arrays are not the same shape.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
