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
    N, Q = inp_li()
    user = [[0] * N for _ in range(N)]
    for _ in range(Q):
        s = inp_li()
        if s[0] == 1:
            user[s[1] - 1][s[2] - 1] = 1
        elif s[0] == 2:
            for i in range(N):
                if user[i][s[1] - 1]:
                    user[s[1] - 1][i] = 1
        else:
            tmp = [0] * N
            for i in user[s[1] - 1]:
                for j in user[i]:
                    tmp[j] = 1
            user[s[1] - 1] = [max(t) for t in zip(user[s[1] - 1], tmp)]
            if user[s[1] - 1][s[1] - 1]:
                user[s[1] - 1][s[1] - 1] = 0
    print("\n".join("".join(list(map(lambda x: "Y" if x else "N", u))) for u in user))


if __name__ == "__main__":
    main()
