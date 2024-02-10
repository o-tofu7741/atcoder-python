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
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = inp_li()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    ans = 0
    for i in range(N):
        if sum(map(lambda x: (x < i), graph[i])) == 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
