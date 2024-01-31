# import bisect
# import collections
# import copy
# import heapq
import itertools

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
    S = inp_s()
    N = len(S)
    ans = [0] * (N + 1)
    for i in range(N):
        if S[i] == "<":
            ans[i + 1] = ans[i] + 1
    # print(ans)
    for i in range(-1, -(N + 1), -1):
        if S[i] == ">":
            if ans[i - 1] < ans[i] + 1:
                ans[i - 1] = ans[i] + 1
    # print(ans)
    print(sum(ans))


if __name__ == "__main__":
    main()
