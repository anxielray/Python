def Transpose(matrix):

    mtrx = []
    row = []
    for x in range(0, len(matrix[0])):
        for r in matrix:
            row.append(row)
        mtrx.append(row)
        row = []

    return mtrx


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    traspose_matrix = Transpose(matrix)
    print(f"The transpose matrix of {matrix} is {transpose_matrix}")
