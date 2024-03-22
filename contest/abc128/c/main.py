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
    n, m = inp_li()
    s = [inp_li()[1:] for _ in range(m)]
    p = inp_li()
    ans = 0
    for i in range(2**n):
        switch_state = [0] * n  # off
        light_state = [0] * m  # off
        for j in range(n):
            if (i >> j) & 1:
                switch_state[j] = 1
        for s_i, s_v in enumerate(s):
            s_cnt = 0
            for j_s in s_v:
                if switch_state[j_s - 1]:
                    s_cnt += 1
            if s_cnt % 2 == p[s_i] and s_cnt:
                light_state[s_i] = 1
        if all(light_state):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
