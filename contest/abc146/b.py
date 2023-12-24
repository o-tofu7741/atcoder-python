N = int(input())
S = input()

# アルファベット順の意味を取り違えてたので不要
# S = "".join(sorted(S))

# 一文字ずつ、アルファベットの番号を求めて26で剰余を求めて大文字に戻す
ans = ""
for s in S:
    ans += chr((ord(s) - ord("A") + N) % 26 + ord("A"))
print(ans)
