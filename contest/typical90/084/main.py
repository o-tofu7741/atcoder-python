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
    # N = inp_i()
    # S = inp_s()
    # group = [(i, len(list(v))) for i, v in itertools.groupby(S)]
    # ans = 0
    # for i in range(2, N + 1):
    #     ans += N - i + 1

    # for i, v in group:
    #     if v > 1:
    #         for j in range(i):
    #             ans -= 0
    print(int(input()) ** 2 - sum(len(t) ** 2 for s in map(input().split, "ox") for t in s) >> 1)
    


if __name__ == "__main__":
    main()
