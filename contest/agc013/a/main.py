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
    ans = 0
    prev = A[0]
    st = 0
    for a in A[1:]:
        if prev < a:
            if st == -1:
                ans += 1
            st = 1
        elif prev > a:
            if st == 1:
                ans += 1
            st = -1
        print(prev, a, st, ans)
        prev = a
    print(ans)


if __name__ == "__main__":
    main()
