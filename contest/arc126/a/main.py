import bisect
import collections
import copy
import heapq
import itertools
import math
import string
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
    n = inp_i()
    for i in range(n):
        ans = 0
        n2, n3, n4 = inp_li()
        x = min(n3 // 2, n4)
        n3 -= x * 2
        n4 -= x
        ans += x
        if min(n2 // 2, n3 // 2) <= min(n2, n4 // 2):
            x = min(n2 // 2, n3 // 2)
            n2 -= x * 2
            n3 -= x * 2
            ans += x
            if n3 > 1 and n4 > 0:
                x = min(n3 // 2, n4)
                n3 -= x * 2
                n4 -= x
                ans += x
        
        print(ans)


if __name__ == "__main__":
    main()
