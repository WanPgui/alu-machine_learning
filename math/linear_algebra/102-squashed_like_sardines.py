#!/usr/bin/env python3
def cat_matrices(mat1, mat2, axis=0):
    from collections.abc import Iterable

    def check_shapes(m1, m2):
        if len(m1) != len(m2):
            return False
        if isinstance(m1[0], list):
            return all(check_shapes(s1, s2) for s1, s2 in zip(m1, m2))
        return True

    def concatenate(m1, m2, axis):
        if axis == 0:
            if len(m1) != len(m2) or (isinstance(m1[0], list) and len(m1[0]) != len(m2[0])):
                return None
            return m1 + m2
        elif axis == 1:
            if len(m1) != len(m2):
                return None
            return [row1 + row2 for row1, row2 in zip(m1, m2)]
        else:
            if len(m1) != len(m2) or any(len(r1) != len(r2) for r1, r2 in zip(m1, m2)):
                return None
            return [concatenate(r1, r2, axis-1) for r1, r2 in zip(m1, m2)]
    
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    if axis < 0:
        return None

    return concatenate(mat1, mat2, axis)
