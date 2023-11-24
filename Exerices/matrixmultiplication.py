import time
import numpy as np

def naive_matrix_mult(A, B):
    m, n = A.shape
    n, p = B.shape
    C = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def strassen_matrix_mult(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B
    else:
        A11 = A[:n//2, :n//2]
        A12 = A[:n//2, n//2:]
        A21 = A[n//2:, :n//2]
        A22 = A[n//2:, n//2:]
        B11 = B[:n//2, :n//2]
        B12 = B[:n//2, n//2:]
        B21 = B[n//2:, :n//2]
        B22 = B[n//2:, n//2:]

        P1 = strassen_matrix_mult(A11 + A22, B11 + B22)
        P2 = strassen_matrix_mult(A21 + A22, B11)
        P3 = strassen_matrix_mult(A11, B12 - B22)
        P4 = strassen_matrix_mult(A22, B21 - B11)
        P5 = strassen_matrix_mult(A11 + A12, B22)
        P6 = strassen_matrix_mult(A21 - A11, B11 + B12)
        P7 = strassen_matrix_mult(A12 - A22, B21 + B22)

        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 - P2 + P3 + P6

        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
        return C


A = np.random.rand(250, 250)
B = np.random.rand(250, 250)

start_time = time.time()
C_naive = naive_matrix_mult(A, B)
naive_time = time.time() - start_time

start_time = time.time()
C_strassen = strassen_matrix_mult(A, B)
strassen_time = time.time() - start_time

print("Naive time: {:.2f}s".format(naive_time))
print("Strassen's time: {:.2f}s".format(strassen_time))