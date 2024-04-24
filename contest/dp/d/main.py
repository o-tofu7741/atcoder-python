import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
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
    N, W = inp_li()
    w = []
    v = []
    for i in range(N):
        wi, vi = inp_li()
        w.append(wi)
        v.append(vi)
    ans = 0
    for i in range(2**N):
        weight = 0
        score = 0
        for j in range(N):
            if (i >> j) & 1:
                weight += w[j]
                score += v[j]
        if weight <= W:
            ans = max(ans, score)
    print(ans)


if __name__ == "__main__":
    main()
