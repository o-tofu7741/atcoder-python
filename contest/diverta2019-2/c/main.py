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
    N = inp_i()
    A = inp_li()
    A_a = [abs(i) for i in A]
    B = []
    while len(A) > 1:
        i = A_a.index(min(A_a))
        j = A_a.index(max(A_a))
        A.append(max(abs(A[i] - A[j])), abs(A[j] - A[i]))
        A_a.append(abs(A[-1]))


if __name__ == "__main__":
    main()
