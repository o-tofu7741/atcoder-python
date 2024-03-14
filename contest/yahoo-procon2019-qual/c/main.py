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
    k, a, b = inp_li()
    if a >= b - 1 or a > k - 1:
        print(k + 1)
    else:
        k -= a - 1
        ans = k // 2 * (b - a) + a
        if k % 2:
            ans += 1
        print(ans)


if __name__ == "__main__":
    main()
