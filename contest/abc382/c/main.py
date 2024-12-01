import bisect
import collections
import copy
import functools
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
    n, m = inp_li()
    a = inp_li()
    b = inp_li()
    eat_lst = [a[0]]
    eat_lst_idx = [0]
    for i in range(1, n):
        if a[i] < eat_lst[-1]:
            eat_lst.append(a[i])
            eat_lst_idx.append(i)
    eat_lst.reverse()
    eat_lst_idx.reverse()
    eat_lst.append(INF)
    eat_lst_idx.append(eat_lst_idx[-1])
    for i in range(m):
        if b[i] < eat_lst[0]:
            print(-1)
        else:
            idx = bisect.bisect_left(eat_lst, b[i])
            if eat_lst[idx] != b[i]:
                idx -= 1
            print(eat_lst_idx[idx] + 1)


if __name__ == "__main__":
    main()
