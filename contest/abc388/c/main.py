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
    n = inp_i()
    A = inp_li()

    ans = 0

    for i in range(n):
        a2 = A[i] * 2
        ans += n - bisect.bisect_left(A, a2)

    print(ans)


if __name__ == "__main__":
    main()
