import sys

N, Y = map(int, input().split())
for a in range(N + 1):
    for b in range(N + 1 - a):
        c = N - (a + b)
        if c >= 0:
            if Y == (a * 10000 + b * 5000 + c * 1000):
                print(f"{a} {b} {c}")
                sys.exit()
print("-1 -1 -1")
