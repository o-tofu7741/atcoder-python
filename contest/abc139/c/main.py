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
    H = inp_li()
    c = 0
    ans = 0
    prev = H[0]
    for h in H[1:]:
        if prev >= h:
            c += 1
        else:
            if ans < c:
                ans = c
            c = 0
        # print(prev, h, c, ans)
        prev = h
    if ans < c:
        ans = c
    print(ans)


if __name__ == "__main__":
    main()
