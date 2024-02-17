# import bisect
# import collections
# import copy
# import heapq
import itertools

# import math
# import string
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
    area = [list(inp_s()) for _ in range(M)]

    j_n_acc = [
        [0] + list(itertools.accumulate(map(lambda x: 1 if x == "J" else 0, lst))) for lst in area
    ]
    o_n_acc = [
        [0] + list(itertools.accumulate(map(lambda x: 1 if x == "O" else 0, lst))) for lst in area
    ]
    # j_m_acc = list(zip(*[[0] + list(itertools.accumulate(lst)) for lst in zip(*j_n_acc)]))
    # o_m_acc = list(zip(*[[0] + list(itertools.accumulate(lst)) for lst in zip(*o_n_acc)]))
    j_mn_acc = [[0] * (N + 1) for _ in range(M + 1)]
    o_mn_acc = [[0] * (N + 1) for _ in range(M + 1)]
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            j_mn_acc[m][n] += j_mn_acc[m - 1][n] + j_n_acc[m - 1][n]
            o_mn_acc[m][n] += o_mn_acc[m - 1][n] + o_n_acc[m - 1][n]

    for _ in range(K):
        ans1 = ans2 = 0
        a, b, c, d = inp_li()
        ans1 = j_mn_acc[c][d] - j_mn_acc[a - 1][d] - j_mn_acc[c][b - 1] + j_mn_acc[a - 1][b - 1]
        ans2 = o_mn_acc[c][d] - o_mn_acc[a - 1][d] - o_mn_acc[c][b - 1] + o_mn_acc[a - 1][b - 1]
        print(ans1, ans2, (c - a + 1) * (d - b + 1) - ans1 - ans2)


if __name__ == "__main__":
    main()
