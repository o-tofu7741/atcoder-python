# import bisect
# import collections
# import copy
# import heapq
# import itertools
# import math
# import string
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
    N, A, B = inp_li()
    S = inp_s()
    ans = []
    a = b = 0
    for i, s in enumerate(S):
        if a + b < A + B:
            if s == "a":
                a += 1
                ans.append("Yes")
            elif s == "b" and b < B:
                b += 1
                ans.append("Yes")
            else:
                ans.append("No")
        else:
            ans.append("No")
    print("\n".join(ans))


if __name__ == "__main__":
    main()
