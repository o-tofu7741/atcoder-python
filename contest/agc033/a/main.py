# import bisect
import collections

# import copy
# import functools
# import heapq
# import itertools
# import math
# import string
import sys

# import numpy

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
    a = [list(inp_s()) for _ in range(h)]
    q = collections.deque([])
    pt = ((0, 1), (1, 0), (-1, 0), (0, -1))
    dist = [[-1] * w for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if a[y][x] == "#":
                q.append((x, y))
                dist[y][x] = 0
    while len(q) > 0:
        x, y = q.popleft()
        for px, py in pt:
            nx = x + px
            ny = y + py
            if 0 <= nx < w and 0 <= ny < h and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((nx, ny))
    print(max(map(max, dist)))


if __name__ == "__main__":
    main()
