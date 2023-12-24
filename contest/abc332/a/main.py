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
    N, S, K = inp_li()
    PQ = [inp_li() for _ in range(N)]
    ans = 0
    for pq in PQ:
        ans += pq[0] * pq[1]
    print(ans if ans >= S else ans + K)


if __name__ == "__main__":
    main()
