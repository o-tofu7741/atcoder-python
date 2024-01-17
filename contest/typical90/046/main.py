# import bisect
import collections

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
    A = []
    B = []
    C = []
    for i in inp_li():
        A.append(i % 46)
    for i in inp_li():
        B.append(i % 46)
    for i in inp_li():
        C.append(i % 46)

    A = collections.Counter(A)
    B = collections.Counter(B)
    C = collections.Counter(C)

    ans = 0

    for a in A:
        for b in B:
            for c in C:
                if (a + b + c) % 46 == 0:
                    ans += A[a] * B[b] * C[c]
    print(ans)


if __name__ == "__main__":
    main()
