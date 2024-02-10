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
    A, B, C = inp_li()

    if B % 4 == 2 and C != 1:
        bc = 0
    elif B % 4 == 3 and C % 2 == 0:
        bc = 1
    else:
        bc = B % 4
    if bc == 0:
        bc = 4
    print((A % 10) ** bc % 10)

    # bc = pow(B, C, 4)
    # if bc == 0:
    #     bc = 4
    # print(pow(A % 10, bc, 10))


if __name__ == "__main__":
    main()
