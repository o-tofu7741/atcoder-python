N, X = map(int, input().split())
A = list(map(int, input().split()))

score = -1

for i in range(101):
    B = A + [i]
    B.sort()
    if X <= sum(B[1:-1]):
        score = i
        break

print(score)
