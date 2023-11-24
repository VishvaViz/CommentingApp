def rotate(matrix):
    n = len(matrix)
    layers = n // 2
    for l in range(layers):
        first, last = l, n - l - 1
        for i in range(first, last):
            top = matrix[l][i]
            matrix[l][i] = matrix[-i - 1][l]
            matrix[-i - 1][l] = matrix[-l - 1][-i - 1]
            matrix[-l - 1][-i - 1] = matrix[i][-l - 1]
            matrix[i][-l - 1] = top
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(matrix)
for row in matrix:
    print(row)