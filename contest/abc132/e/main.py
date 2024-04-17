# import bisect
import collections
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
    g1 = [[0] * n for _ in range(n)]
    g2 = [[0] * n for _ in range(n)]
    for i in range(m):
        u, v = inp_li()
        g1[u - 1][v - 1] = 1
    s, t = inp_li()
    s -= 1
    t -= 1

    for i in range(n):
        # 件検波1
        for j1 in range(n):
            if g1[i][j1]:
                # 件検波2
                for j2 in range(n):
                    if g1[j1][j2]:
                        # 件検波3
                        for j3 in range(n):
                            if g1[j2][j3] and i != j3:
                                g2[i][j3] = 1

    q = collections.deque([])
    q.append(s)
    ans = [INF] * n
    ans[s] = 0

    while q:
        now = q.popleft()
        for i in range(n):
            if g2[now][i] and now != i:
                if ans[i] == INF:
                    ans[i] = ans[now] + 1
                    q.append(i)
    if ans[t] == INF:
        print(-1)
    else:
        print(ans[t])


if __name__ == "__main__":
    main()
