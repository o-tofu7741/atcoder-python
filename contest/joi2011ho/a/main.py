import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys

# import numpy


def inp_i():
    return int(sys.stdin.readline().rstrip())


def inp_li():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def inp_s():
    return sys.stdin.readline().rstrip()


def inp_ls():
    return list(sys.stdin.readline().rstrip().split())


def main():
    M, N = inp_li()
    K = inp_i()
    # numpyを用いた二次元累積和
    # J = [[0] + [0 for j in range(N)] for i in range(M)]
    # O = [[0] + [0 for j in range(N)] for i in range(M)]
    # I = [[0] + [0 for j in range(N)] for i in range(M)]
    Area = [list(inp_s()) for _ in range(M)]
    J = [[0] + list(itertools.accumulate(map(lambda x: 1 if x == "J" else 0, lst))) for lst in Area]
    O = [[0] + list(itertools.accumulate(map(lambda x: 1 if x == "O" else 0, lst))) for lst in Area]
    # # 繰り返し処理を用いて累積和にJOIの個数を格納
    # for i in range(M):
    #     sum1 = 0
    #     sum2 = 0
    #     # sum3 = 0
    #     for j in range(N):
    #         if Area[i][j] == "J":
    #             sum1 += 1
    #         if Area[i][j] == "O":
    #             sum2 += 1
    #         # if Area[i][j] == "I":
    #         #     sum3 += 1
    #         J[i][j + 1] = sum1
    #         O[i][j + 1] = sum2
    #         # I[i][j + 1] = sum3
    # print(J)
    for _ in range(K):
        ans1 = ans2 = 0
        a, b, c, d = inp_li()
        for m in range(a - 1, c):
            ans1 = ans1 + J[m][d] - J[m][b - 1]
            ans2 = ans2 + O[m][d] - O[m][b - 1]
            # ans3 = ans3 + I[m][d] - I[m][b - 1]
        print(ans1, ans2, (c - a + 1) * (d - b + 1) - ans1 - ans2)


if __name__ == "__main__":
    main()
