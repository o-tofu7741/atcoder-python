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
    H = inp_li()
    peak = [1] * N
    for _ in range(M):
        A, B = inp_li()
        A -= 1
        B -= 1
        if H[A] == H[B]:
            peak[A] = peak[B] = 0
        elif H[A] < H[B]:
            peak[A] = 0
        else:
            peak[B] = 0
    print(sum(peak))


if __name__ == "__main__":
    main()
