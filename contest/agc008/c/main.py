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
    i, o, _, j, l, _, _ = inp_li()
    k1 = (i // 2) * 2 + o + (j // 2) * 2 + (l // 2) * 2
    k2 = (
        (((i - 1) // 2) * 2 if i else 0)
        + o
        + (((j - 1) // 2) * 2 if j else 0)
        + (((l - 1) // 2) * 2 if l else 0)
    )
    if all([i, j, l]):
        k2 += 3
    print(max(k1, k2))


if __name__ == "__main__":
    main()
