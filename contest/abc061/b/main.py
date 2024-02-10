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
    N, M = inp_li()
    ans = [0] * N
    for m in range(M):
        a, b = inp_li()
        ans[a - 1] += 1
        ans[b - 1] += 1
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
