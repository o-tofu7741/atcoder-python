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
    N, X, M = inp_li()
    last = -1
    A = [X]
    for i in range(N - 1):
        last = A[-1] ** 2 % M
        if last in A:
            break
        A.append(last)
    else:
        print(sum(A))
        sys.exit()

    last_i = A.index(last)
    cycle = A[last_i:]
    no_dup = A[:last_i]
    print(
        sum(no_dup)
        + sum(cycle) * ((N - len(no_dup)) // len(cycle))
        + sum(A[last_i : last_i + (N - len(no_dup)) % len(cycle)])
    )


if __name__ == "__main__":
    main()
