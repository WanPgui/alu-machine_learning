def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.
        axis (int, optional): The axis along which to concatenate. Defaults to 0.

    Returns:
        list: The concatenated matrix, or None if concatenation is not possible.
    """
    # Convert the input matrices to NumPy arrays
    np_mat1 = np.array(mat1)
    np_mat2 = np.array(mat2)

    # Check if the matrices can be concatenated along the specified axis
    if np_mat1.shape[axis] != np_mat2.shape[axis]:
        return None

    # Concatenate the matrices using NumPy's concatenate function
    concatenated_mat = np.concatenate((np_mat1, np_mat2), axis=axis)

    # Convert the concatenated matrix back to a list
    concatenated_mat_list = concatenated_mat.tolist()

    return concatenated_mat_list