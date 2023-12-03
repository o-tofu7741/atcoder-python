def main():
    N, Q = map(int, input().split())
    S = input()
    LR = []
    for _ in range(Q):
        LR.append(list(map(int, input().split())))

    S = list(S)
    c = []
    for i in range(N - 1):
        c.append(1 if len({S[i], S[i + 1]}) == 1 else 0)
    accum = [0]
    for i in c:
        accum.append(accum[-1] + i)
    # accum = accum[1:]
    for lr in LR:
        l, r = lr[0], lr[1]
        # print(accum)
        print(accum[r - 1] - accum[l - 1])


main()
