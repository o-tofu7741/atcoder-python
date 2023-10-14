n = int(input())
a = list(map(int, input().split()))
print("Yes" if len(a) == a.count(a[0]) else "No")
