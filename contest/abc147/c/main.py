import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys

# import numpy

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
    xy = []
    for i in range(n):
        xy.append([inp_li() for _ in range(inp_i())])
    ans = 0
    for i in range(2**n):
        honest = []
        for j in range(n):
            if (i >> j) & 1:
                honest.append(j)
        for k in honest:
            for x, y in xy[k]:
                if not (y and x-1 in honest or not y and x-1 not in honest):
                    break
            else:
                continue
            break
        else:
            ans = max(ans, len(honest))

    print(ans)


if __name__ == "__main__":
    main()
