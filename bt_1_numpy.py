import numpy as np
from sympy import *


def matrix(m, n):
    A = np.random.randint(0, 10, size=n*m).reshape(m, n)
    #print('ma trận a: \n', A)
    return A


def rank_matran(A):
    rank_A = np.linalg.matrix_rank(A)
    #print(f'rank = {rank_A}')
    return rank_A


def bac_thang(A):
    M = Matrix(A)
    # Use sympy.rref() method
    M_rref = M.rref()
    #print('Ma trận bậc thang: \n', M_rref)
    return np.array(M_rref[0])


def main():
    a = matrix(3,4)
    r = rank_matran(a)
    b = bac_thang(a)
    print(a)
    print(r)
    print(b)

if __name__ == '__main__':
     main()