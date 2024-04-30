import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
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
    h, w = inp_li()
    q = collections.deque([])
    pt = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    hw = []
    grid = [[-1] * w for _ in range(h)]
    for i in range(h):
        s = inp_s()
        for j in range(w):
            if s[j] == "#":
                q.append([i, j])
                grid[i][j] = 0
        hw.append(list(s))
    ans = 1
    while q:
        i, j = q.popleft()
        for pi, pj in pt:
            ni = i + pi
            nj = j + pj
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == -1:
                grid[ni][nj] = grid[i][j] + 1
                if ans < grid[ni][nj]:
                    ans = grid[ni][nj]
                q.append([ni, nj])
    if ans <= 1:
        print(1)
        exit()
    q2 = collections.deque([])
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] > 1:
                q2.append([i, j])
                tmp = 0
                while q2:
                    ii, jj = q2.popleft()
                    for pi, pj in pt:
                        ni = ii + pi
                        nj = jj + pj
                        if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] > 0:
                            tmp += 1
                            if grid[ni][nj] > 1:
                                q2.append([ni, nj])
                            grid[ni][nj] = 0
                count = max(count, tmp)
    print(count)


if __name__ == "__main__":
    main()
