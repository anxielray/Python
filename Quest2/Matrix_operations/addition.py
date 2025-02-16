def add_matrices(matrix1, matrix2):
    """
    Adds two 3x3 matrices with input validation.

    Args:
        matrix1: The first 3x3 matrix (list of lists).
        matrix2: The second 3x3 matrix (list of lists).

    Returns:
        A new 3x3 matrix representing the sum of the input matrices,
        or None if the input is invalid.
    """

    # Input validation checks
    if not isinstance(matrix1, list) or not isinstance(matrix2, list):
        print("Error: Input must be lists.")
        return None

    if len(matrix1) != 3 or len(matrix2) != 3:
        print("Error: Matrices must have 3 rows.")
        return None

    for row in matrix1:
        if not isinstance(row, list) or len(row) != 3:
            print("Error: Each row in matrix1 must be a list of 3 elements.")
            return None
        if not all(isinstance(element, (int, float)) for element in row):
            print("Error: Elements in matrix1 must be numbers.")
            return None

    for row in matrix2:
        if not isinstance(row, list) or len(row) != 3:
            print("Error: Each row in matrix2 must be a list of 3 elements.")
            return None
        if not all(isinstance(element, (int, float)) for element in row):
            print("Error: Elements in matrix2 must be numbers.")
            return None

    # Perform matrix addition if input is valid
    result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initialize result matrix

    for i in range(3):
        for j in range(3):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix


# Example usage:
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrix_c = [[9, 8, 7], [6, 5, 4]]

matrix_d = [[9, 8, "seven"], [6, 5, 4], [3, 2, 1]]


result = add_matrices(matrix_a, matrix_b)
if result:
    print("Matrix A + Matrix B:")
    for row in result:
        print(row)

result = add_matrices(matrix_a, matrix_c)
if result:
    print("Matrix A + Matrix C:")
    for row in result:
        print(row)

result = add_matrices(matrix_a, matrix_d)
if result:
    print("Matrix A + Matrix D:")
    for row in result:
        print(row)
