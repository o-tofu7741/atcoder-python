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
    h = inp_li()

    for i in range(n):
        if h[0] < h[i]:
            print(i + 1)
            exit()
    print(-1)


if __name__ == "__main__":
    main()
