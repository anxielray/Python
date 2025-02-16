def vector_multiply(vector1, vector2):
    """
    Performs element-wise vector multiplication of two vectors.

    Args:
        vector1: The first vector (list of numbers).
        vector2: The second vector (list of numbers).

    Returns:
        A new vector (list) representing the element-wise product of the
        input vectors, or None if the input is invalid.
    """

    # Input Validation
    if not isinstance(vector1, list) or not isinstance(vector2, list):
        print("Error: Both inputs must be lists (vectors).")
        return None

    if not all(isinstance(element, (int, float)) for element in vector1):
        print("Error: All elements in vector1 must be numbers (int or float).")
        return None

    if not all(isinstance(element, (int, float)) for element in vector2):
        print("Error: All elements in vector2 must be numbers (int or float).")
        return None

    if len(vector1) != len(vector2):
        print(
            "Error: Vectors must have the same length for element-wise multiplication."
        )
        return None

    if not vector1 or not vector2:
        print("Warning: One or both input vectors are empty. Returning an empty list")
        return []

    # Element-wise multiplication
    result_vector = []
    for i in range(len(vector1)):
        result_vector.append(vector1[i] * vector2[i])

    return result_vector


# Example Usage:
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
vector_c = [4, 5]

result = vector_multiply(vector_a, vector_b)

if result:
    print("Vector A:", vector_a)
    print("Vector B:", vector_b)
    print("Element-wise Product:", result)

result = vector_multiply(vector_a, vector_c)
if result == None:
    print("Multiplication failed due to size differences.")

# Another test
vector_d = [1, 2, "three"]

result = vector_multiply(vector_a, vector_d)
if result == None:
    print("Multiplication failed due to type issues.")
