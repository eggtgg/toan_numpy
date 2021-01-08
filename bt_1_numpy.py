import numpy as np
from sympy import *


def matrix(n, m):
    a = np.random.randint(0, 10, size=n*m).reshape(n, m)
    print('ma trận a: \n', a)
    return a


def rank_matran(a):
    rank_a = np.linalg.matrix_rank(a)
    print(f'rank = {rank_a}')
    return rank_a


def bac_thang(a):
    M = Matrix(a)
    # Use sympy.rref() method
    M_rref = M.rref()
    print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))


def main():
    b = matrix(4,5)
    rank_matran(b)
    bac_thang(b)


if __name__ == '__main__':
     main()