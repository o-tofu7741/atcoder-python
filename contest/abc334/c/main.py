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
    N, K = inp_li()
    A = sorted(inp_li())
    n = sorted([i for i in range(1, N + 1)] + A)
    ans = 0
    pi = pj = 0
    for i, j in zip(n[::2], n[1::2]):
        ans += abs(i - j)
    print(ans)


if __name__ == "__main__":
    main()
