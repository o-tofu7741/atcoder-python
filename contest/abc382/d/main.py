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
    lst = []
    lst_str = []
    for i in range(n):
        
    for i in range(1,m-20+1):
        for j in range(i+1,m-10+1):
            for k in range(j+1,m+1):
                s = int(str(i)+str(j)+str(k))
                idx = bisect.bisect_left(lst, s)
                if idx == len(lst) or len(lst) == 0:
                    lst.insert(idx, s)
                    lst_str.insert(idx, [i,j,k])
                elif lst[idx] != s:
                    lst.insert(idx, s)
                    lst_str.insert(idx, [i,j,k])
    for i in range(len(lst)):
        print(*lst_str[i])



def check(a, b):
    for i, j in zip(a, b):
        if i == j:
            continue
        elif i > j:
            return -1
    if a[-1] == b[-1]:
        return 0
    return 1


if __name__ == "__main__":
    main()
