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
    N, M = inp_li()
    sima = [[] for _ in range(N)]
    ans = "IMPOSSIBLE"
    for _ in range(M):
        a, b = inp_li()
        a -= 1
        b -= 1
        sima[a].append(b)
        # sima[b].append(a)
    for i in sima[0]:
        for j in sima[i]:
            if j == N - 1:
                ans = "POSSIBLE"
    print(ans)


if __name__ == "__main__":
    main()
