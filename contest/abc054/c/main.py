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
    N, M = inp_li()
    graph = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b = inp_li()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    zero = [[0] + list(lst) for lst in itertools.permutations([i for i in range(1, N)])]

    ans = 0
    for z in zero:
        for i in range(1, N):
            if z[i] not in graph[z[i - 1]]:
                break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
