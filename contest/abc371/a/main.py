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
    ab,ac,bc =inp_ls()
    abc =[0,0,0]
    if ab == ">":
        abc[0]+=1
    else:
        abc[1]+=1
    if ac == ">":
        abc[0]+=1
    else:
        abc[2]+=1
    if bc ==">":
        abc[1]+=1
    else:
        abc[2]+=1
    for i in range(3):
        if abc[i] == 1:
            print("ABC"[i])


if __name__ == "__main__":
    main()
