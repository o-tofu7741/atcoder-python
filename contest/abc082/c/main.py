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
    A = inp_li()

    num = collections.Counter(A)
    ans = 0
    for key in num:
        if num[key] >= key:
            ans += num[key] - key
        else:
            ans += num[key]
    print(ans)


if __name__ == "__main__":
    main()
