def matrix_transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]