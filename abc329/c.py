def main():
    N = int(input())
    S = input()
    i = 0
    counts = {}
    while i < N:
        c = 1
        while i + 1 < N and S[i] == S[i + 1]:
            c += 1
            i += 1
        if counts.get(S[i], 0) < c:
            counts[S[i]] = c
        i += 1
    print(sum(counts.values()))


main()
