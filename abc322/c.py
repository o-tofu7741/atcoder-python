N, M = map(int, input().split())
A = list(map(int, input().split()))

day = 0
ans = []
for i in A:
    ans += [f"{j}" for j in range(i - day - 1, -1, -1)]
    day = i

print("\n".join(ans))
