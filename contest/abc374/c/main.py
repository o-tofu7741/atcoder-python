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
    n = inp_i()
    k = inp_li()

    s = sum(k)
    ans=INF
    for i in range(1,n):
        for comb in itertools.combinations(k,i):
            a = sum(comb)
            b = s-a
            ans = min(ans,max(a,b))
    print(ans)



if __name__ == "__main__":
    main()
