# import bisect
# import collections
# import copy
# import functools
# import heapq
# import itertools
# import math
# import string
import sys

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
    n, m = inp_li()
    g = [[] for _ in range(n)]
    g2 = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = inp_li()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
        g2[a - 1][b - 1] = 1
        g2[b - 1][a - 1] = 1
    ans = 0
    for i in range(n):
        # 1人目
        for j in g[i]:
            # 2人目
            for k in g[j]:
                if k != i and g2[i][k] == 0:
                    g[i].append(k)
                    g[k].append(i)
                    g2[i][k] = 1
                    g2[k][i] = 1
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
