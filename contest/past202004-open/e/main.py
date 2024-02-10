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
    N = inp_i()
    A = inp_li()
    pt = []
    c = 0
    i = -1
    while c < N:
        i += 1
        if A[i] != i + 1:
            for p in pt:
                if A[i] in p:
                    break
            else:
                j = i
                tmp = []
                while A[j] not in tmp:
                    tmp.append(A[j])
                    j = A[j] - 1
                pt.append(tmp)
                c += len(tmp)
        else:
            c += 1
        print(pt, c, i)
    print(pt)
    ans = []
    for i in range(N):
        if i + 1 == A[i]:
            ans.append(1)
        else:
            for p in pt:
                if i + 1 in p:
                    ans.append(len(p))
    print(*ans)


if __name__ == "__main__":
    main()
