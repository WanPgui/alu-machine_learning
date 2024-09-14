#!/usr/bin/env python3

def add_matrices(mat1, mat2):
    # Check if both matrices have the same shape
    if len(mat1) != len(mat2) or (isinstance(mat1[0], list) and len(mat1[0]) != len(mat2[0])):
        return None

    # Check if matrices are nested lists or not
    if isinstance(mat1[0], list):
        # Recursive call for nested matrices
        return [add_matrices(sub1, sub2) for sub1, sub2 in zip(mat1, mat2)]
    else:
        # Element-wise addition for non-nested lists (flat matrices)
        return [x + y for x, y in zip(mat1, mat2)]
