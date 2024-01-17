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
    A = [inp_s() for _ in range(N)]
    S = set()
    for i in A:
        S = S.union(set(list(i)))

    ans = {}
    for a in A:
        num = collections.Counter(a)
        for s in S:
            if num[s] < ans.get(s, 51):
                ans[s] = num[s]

    a = ''
    for k, v in sorted(ans.items()):
        a += k * v
    print(a)


if __name__ == "__main__":
    main()
