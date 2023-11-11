N = int(input())
D = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    if len(set(list(str(i)))) == 1:
        tmp = i % 10
        if tmp <= D[i - 1]:
            ans += 1
        if tmp * 10 + tmp <= D[i - 1]:
            ans += 1
            if (tmp * 10 + tmp) * 10 + tmp <= D[i - 1]:
                ans += 1
    else:
        continue

print(ans)
