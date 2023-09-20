import math


def calc_distance(a, b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    return math.sqrt(sum)


N, D = map(int, input().split())
X = []
ans = 0
for i in range(N):
    X.append(list(map(int, input().split())))
for i in range(N):
    for j in range(i + 1, N):
        if calc_distance(X[i], X[j]) % 1 == 0:
            ans += 1
print(ans)
