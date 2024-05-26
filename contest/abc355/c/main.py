import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

INF = 10**18


def inp_i():
    return int(sys.stdin.readline().rstrip())


def inp_li():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def inp_s():
    return sys.stdin.readline().rstrip()


def inp_ls():
    return list(sys.stdin.readline().rstrip().split())


def main():
    n, t = inp_li()
    a = inp_li()
    grid = [[0] * n for _ in range(n)]
    holes = [0] * (n * (n - 1) + n + 1)
    for i in range(n):
        for j in range(n):
            holes[n * (i) + j + 1] = (i, j)
    for k in range(t):
        hit = a[k]
        i, j = holes[hit]
        grid[i][j] = 1
        for ii in range(n):
            if grid[i][ii] == 0:
                break
        else:
            print(k + 1)
            exit()
        for jj in range(n):
            if grid[jj][j] == 0:
                break
        else:
            print(k + 1)
            exit()
        for ij in range(n):
            if grid[ij][ij] == 0:
                break
        else:
            print(k + 1)
            exit()
        for ji in range(n):
            if grid[ji][n - ji - 1] == 0:
                break
        else:
            print(k + 1)
            exit()
    print(-1)


if __name__ == "__main__":
    main()
