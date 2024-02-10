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
    N, K = inp_li()
    P = inp_li()
    C = inp_li()
    ans = -1000000000

    cycles = []
    for i in range(N):
        for cy in cycles:
            if P[i] in cy:
                break
        else:
            tmp = []
            j = i
            while P[j] not in tmp:
                tmp.append(P[j])
                j = P[j] - 1
            cycles.append(tmp)
    # print(cycles)
    for cy in cycles:
        scores = [C[i - 1] for i in cy]
        scores2 = scores + scores
        # acm = [0] + list(itertools.accumulate(scores2))
        if len(scores) < K:
            if sum(scores) > 0:
                k = K % len(scores)
                max_sum_cy = 0
                if k != 0:
                    for i in range(len(scores)):
                        max_sum_cy = max(max_sum_cy, max(itertools.accumulate(scores2[i : i + k])))
                    ans = max(ans, sum(scores) * (K // len(scores)) + max_sum_cy)
                else:
                    for i in range(len(scores)):
                        max_sum_cy = max(
                            max_sum_cy, max(itertools.accumulate(scores2[i : i + len(scores)]))
                        )
                    ans = max(ans, sum(scores) * (K // len(scores) - 1) + max_sum_cy)
            else:
                for i in range(len(scores)):
                    ans = max(ans, max(itertools.accumulate(scores2[i : i + len(scores)])))
        else:
            for i in range(len(scores)):
                ans = max(ans, max(itertools.accumulate(scores2[i : i + K])))
    print(ans)


if __name__ == "__main__":
    main()
