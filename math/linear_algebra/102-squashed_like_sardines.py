#!/usr/bin/env python3
"""
Module to concatenate two matrices along a specific axis.
"""

def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specified axis.

    Args:
        mat1 (list of list): The first matrix.
        mat2 (list of list): The second matrix.
        axis (int, optional): The axis along which to concatenate. Default is 0.

    Returns:
        list of list: The concatenated matrix, or None if concatenation fails.
    """
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    def check_dimensions(matrix):
        """
        Checks the dimensions of a matrix.

        Args:
            matrix (list of list): The matrix to check.

        Returns:
            tuple: A tuple representing the shape of the matrix.
        """
        shape = []
        while isinstance(matrix, list):
            shape.append(len(matrix))
            matrix = matrix[0] if matrix else []
        return tuple(shape)

    shape1 = check_dimensions(mat1)
    shape2 = check_dimensions(mat2)

    if shape1 == shape2:
        def concatenate_along_axis(mat1, mat2, axis):
            """
            Concatenates two matrices along a specified axis.

            Args:
                mat1 (list of list): The first matrix.
                mat2 (list of list): The second matrix.
                axis (int): The axis along which to concatenate.

            Returns:
                list of list: The concatenated matrix.
            """
            if axis == 0:
                return mat1 + mat2
            elif axis == 1:
                if len(mat1) != len(mat2):
                    return None
                return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
            else:
                return None

        return concatenate_along_axis(mat1, mat2, axis)

    return None

