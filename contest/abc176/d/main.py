import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

import numpy

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
    ch, cw = inp_li()
    dh, dw = inp_li()
    s = [list(inp_s()) for _ in range(h)]

    deq = collections.deque([])
    deq.append((cw - 1, ch - 1))
    pt_walk = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    pt_warp = list(itertools.product([-2, -1, 0, 1, 2], repeat=2))
    dist = [[INF] * w for _ in range(h)]
    dist[ch - 1][cw - 1] = 0

    while deq:
        x, y = deq.popleft()
        for px, py in pt_walk:
            nx = x + px
            ny = y + py
            if (
                0 <= nx < w
                and 0 <= ny < h
                and s[ny][nx] == "."
                and dist[ny][nx] > dist[y][x]
            ):
                dist[ny][nx] = dist[y][x]
                deq.appendleft((nx, ny))
        for px, py in pt_warp:
            nx = x + px
            ny = y + py
            if (
                0 <= nx < w
                and 0 <= ny < h
                and s[ny][nx] == "."
                and dist[ny][nx] > dist[y][x] + 1
            ):
                dist[ny][nx] = dist[y][x] + 1
                deq.append((nx, ny))
    print(dist[dh - 1][dw - 1] if dist[dh - 1][dw - 1] != INF else -1)


if __name__ == "__main__":
    main()
