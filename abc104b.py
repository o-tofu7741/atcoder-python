# 判定関数
def isAC(S):
    # Sの先頭が"A"でない場合はFalse
    if S[0] != "A":
        return False

    # Sの先頭2文字と末尾1文字を除いた"c"の個数を調べる
    if S[2:-1].count("C") != 1:
        return False

    # Sに含まれる大文字の個数を調べる
    if sum(map(str.isupper, S)) != 2:
        return False

    # 条件をすべて満たせばTrue
    return True


# 入力して判定して出力
print("AC" if isAC(input()) else "WA")
