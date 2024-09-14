#!/usr/bin/env python3
"""
Perform n-dimensional matrix addition.
"""

def add_matrices(mat1, mat2):
    """
    Add two matrices element-wise by dimension.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.

    Returns:
        list: The element-wise sum of the two matrices.
              Returns None if matrices cannot be added.
    """
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    # Helper function to recursively add matrices
    def add_recursive(m1, m2):
        if isinstance(m1, (int, float)) and isinstance(m2, (int, float)):
            return m1 + m2
        if len(m1) != len(m2):
            return None
        if isinstance(m1[0], (int, float)) != isinstance(m2[0], (int, float)):
            return None
        result = []
        for sub1, sub2 in zip(m1, m2):
            added = add_recursive(sub1, sub2)
            if added is None:
                return None
            result.append(added)
        return result

    return add_recursive(mat1, mat2)

