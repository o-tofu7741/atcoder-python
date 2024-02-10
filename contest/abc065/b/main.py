# import bisect
# import collections
# import copy
# import heapq
# import itertools
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
    N = inp_i()
    A = [inp_i() for i in range(N)]

    # 現在のボタン状況
    ans = [1] + [0 for i in range(N - 1)]
    # 正解のボタン状況
    hit = [0, 1] + [0 for i in range(N - 2)]

    i = c = 0
    flag = False

    while c < N:
        ans[i] = 0
        ans[A[i] - 1] = 1
        i = A[i] - 1
        c += 1
        if ans == hit:
            flag = True
            break
    print(c if flag else "-1")


if __name__ == "__main__":
    main()
