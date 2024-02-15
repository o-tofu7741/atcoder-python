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
    A = [0]
    B = [0]
    X = [0]
    for _ in range(N - 1):
        a, b, x = inp_li()
        A.append(a)
        B.append(b)
        X.append(x)
    accm = [0] + list(itertools.accumulate(A))
    # print(N, len(accm))
    stage = 1
    prev = 0
    time = 0

    while stage < N:
        if B[stage] < (accm[X[stage]] - accm[prev]):
            time += B[stage]
            prev = stage
            stage = X[stage]
        else:
            time += A[stage]
            prev = stage
            stage += 1
    print(time)


if __name__ == "__main__":
    main()
