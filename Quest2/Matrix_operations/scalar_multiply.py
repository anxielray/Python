def scalar_multiply_matrix(matrix, scalar):
    """
    Performs scalar multiplication on a matrix.

    Args:
        matrix: A list of lists representing the matrix.
        scalar: The scalar value to multiply the matrix by.

    Returns:
        A new matrix representing the scalar multiplied matrix,
        or None if the input is invalid.
    """

    # Input validation checks
    if not isinstance(matrix, list):
        print("Error: Input must be a list of lists (matrix).")
        return None

    if not all(isinstance(row, list) for row in matrix):
        print("Error: Each element in the matrix must be a list (row).")
        return None

    # Check if the matrix is empty
    if not matrix:
        print("Warning: Input matrix is empty.  Returning an empty matrix.")
        return []

    # Ensure all rows have the same length (matrix property)
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        print("Error: All rows in the matrix must have the same length.")
        return None

    # Ensure elements are numbers
    for row in matrix:
      if not all(isinstance(element, (int, float)) for element in row):
        print("Error: All elements in the matrix must be numbers (int or float).")
        return None

    if not isinstance(scalar, (int, float)):
        print("Error: Scalar must be a number (int or float).")
        return None
    # Perform scalar multiplication
    result_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j] * scalar)
        result_matrix.append(row)

    return result_matrix


# Example Usage
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

scalar_value = 2.5

result = scalar_multiply_matrix(matrix_a, scalar_value)

if result:
    print("Original Matrix:")
    for row in matrix_a:
        print(row)
    print(f"\nScalar: {scalar_value}")
    print("\nScalar-Multiplied Matrix:")
    for row in result:
        print(row)
else:
    print("Scalar multiplication failed due to invalid input.")

# Example of invalid input
bad_matrix = [
    [1, 2, "three"],
    [4, 5, 6]
]

result = scalar_multiply_matrix(bad_matrix, 2)

