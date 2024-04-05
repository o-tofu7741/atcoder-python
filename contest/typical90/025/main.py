import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

# import numpy

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
    n, b = inp_li()
    dfs()


def dfs(num_str, next):
    if len(num_str) == 11:
        return
    else:
        for i in range(next, 10):
            num_str2 = num_str + str(i)
            dfs(num_str2, i)


if __name__ == "__main__":
    main()
