# -*- coding: utf-8 -*-

"""
Created: Oct. 18th, 2018
Implementation of the naive MatrixProduct algorithm
Author: Arthur Journe
"""

import numpy as np

# Type: Naive algorithm
# Complexity: O(n³)
# Efficient for: small matrix, pretty inefficient

def MatrixProduct(A, B):
    """
        Computes the matrix product of same size square matrix A and B. Naive method.
        Input : A, B numpy arrays. Shape (n, n)
        Output: C, numpy array result of A*# B
    """
    if (np.shape(A) != np.shape(B)) or (np.shape(A)[0] !=  np.shape(A)[1]) or (np.shape(B)[0] !=  np.shape(B)[1]):
        print("Error in the shape of the matrix.")
        exit()
    n = np.shape(A)[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            c = 0
            for k in range(n):
                c += A[i][k]*B[k][j]
            C[i][j] = c
    return C
