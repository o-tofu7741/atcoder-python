S = input()

while len(S) > 2:
    S = S[:-2]
    if S[: len(S) // 2] == S[len(S) // 2:]:
        break

print(S)
