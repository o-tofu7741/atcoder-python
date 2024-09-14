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
    n,m = inp_li()
    house = [0]*(n+1)
    for _ in range(m):
        a,b =inp_ls()
        a= int(a)
        if b == "M":
            if house[a]==0:
                house[a]=1
                print("Yes")
                continue
        print("No")





if __name__ == "__main__":
    main()
