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
    a = [0] + inp_li()
    ans = 0
    pt = []
    while sum(a) != 0:
        for i, v in enumerate(a):
            if i != v and v != 0:
                ans += 1
                pt.append((i, v) if i < v else (v, i))
                if i == a[v]:
                    a[i] = a[v] = 0
                else:
                    tmp = a[v]
                    a[v] = 0
                    a[i] = tmp
            else:
                a[i] = 0
            # print(a)

    print(ans)
    for p in pt:
        print(*p)


if __name__ == "__main__":
    main()
