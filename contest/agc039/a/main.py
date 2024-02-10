# import bisect
# import collections
# import copy
# import heapq
import itertools

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
    S = inp_s()
    K = inp_i()
    g = [(i, len(list(v))) for i, v in itertools.groupby(S)]
    ans = 0
    for i, v in g:
        ans += v // 2
    ans *= K

    if S[0] == S[-1] and g[0][1] % 2 == 1 and g[-1][1] % 2 == 1:
        if len(g) == 1:
            ans += K // 2
        else:
            ans += K - 1
    print(ans)


if __name__ == "__main__":
    main()
