N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

st = [[i for i in range(N)]] * N
c = [0] * N
for i in range(M):
    c[A[i]] += 1

