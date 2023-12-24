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
    A = inp_li()
    count = 0
    i = 0
    for j in range(N):
        A[j] = int(A[j])
    while 0 <= count:
        x = i % N
        if A[x] % 2 == 0:
            A[x] = A[x] / 2
            if x == N - 1:
                count += 1
            i += 1
        else:
            print(count)
            count = -1


if __name__ == "__main__":
    main()
