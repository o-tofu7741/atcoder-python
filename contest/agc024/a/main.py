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
    a, b, c, k = inp_li()
    print("Unfair" if abs(a - b) > 10**18 else b - a if k % 2 else a - b)


if __name__ == "__main__":
    main()
