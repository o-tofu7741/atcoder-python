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
    n = inp_i()
    a = inp_li()
    q = collections.deque([a[0]])
    for i in range(n - 1):
        q.appendleft(a[i + 1])
        while True:
            if len(q) <= 1:
                break
            r1 = q.popleft()
            r2 = q.popleft()
            if r1 != r2:
                q.appendleft(r2)
                q.appendleft(r1)
                break
            else:
                q.appendleft(r1 + 1)

    print(len(q))


if __name__ == "__main__":
    main()
