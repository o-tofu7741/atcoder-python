# import bisect
# import collections
# import copy
# import functools
# import heapq
# import itertools
# import math
# import string
import sys

INF = 10**18


def inp_i():
    return int(sys.stdin.readline().rstrip())


def inp_li():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def inp_s():
    return sys.stdin.readline().rstrip()


def inp_ls():
    return list(sys.stdin.readline().rstrip().split())


def main():
    n = inp_i()
    ac = [[i] + inp_li() for i in range(n)]

    # acs = set([i for i in range(n)])
    aa = sorted(ac, key=lambda x: x[1],reverse=True)

    mn = INF
    ans = []

    for i in range(n):
        n, a, c = aa[i]
        if c < mn:
            ans.append(n + 1)
            mn = c
    print(len(ans))
    print(*sorted(ans))


if __name__ == "__main__":
    main()
