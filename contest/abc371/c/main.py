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
    mg= inp_i()
    g=[[]*(n+1) for _ in range(n+1)]
    for _ in range(mg):
        u,v= inp_li()
        g[u].append(v)
        g[v].append(u)
    mh=inp_i()
    h =[[0]*(n+1) for _ in range(n+1)]
    for _ in range(mh):
        a,b=inp_li()
        h[a].append(b)
        h[b].append(a)
    cost = [[-1]*(n+1) for _ in range(n+1)]
    for i in range(1,n):
        for k,v in enumerate(inp_li()):
            j = i+k+1
            cost[i][j]=v
    pt = list(itertools.permutations(range(1,n+1)))
    ans = INF
    for a in pt:
        for b in pt:
            tmp_ans = 0
            for x in a:
                pass




if __name__ == "__main__":
    main()
