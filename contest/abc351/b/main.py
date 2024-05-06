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
    n = inp_i()
    a = [list(inp_s()) for _ in range(n)]
    b = [list(inp_s()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                print(i + 1, j + 1)
                exit()


if __name__ == "__main__":
    main()
