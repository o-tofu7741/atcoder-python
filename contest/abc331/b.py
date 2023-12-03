N, S, M, L = map(int, input().split())
ans = 10**18
for s in range(0, -(-N // 6) + 1):
    for m in range(0, -(-N // 8) + 1):
        for l in range(0, -(-N // 12) + 1):
            if s * 6 + m * 8 + l * 12 >= N:
                tmp = S * s + M * m + L * l
                if ans > tmp:
                    ans = tmp
print(ans)
