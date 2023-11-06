B = int(input())

for i in range(1, B + 1):
    n = pow(i, i)
    if n == B:
        print(i)
        break
    elif n < B:
        continue
    else:
        print(-1)
        break
