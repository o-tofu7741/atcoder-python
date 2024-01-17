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
    M = [inp_s() for _ in range(N)]
    s = set()
    for i, v in enumerate(M):
        if v not in s:
            print(i + 1)
            s.add(v)


if __name__ == "__main__":
    main()
