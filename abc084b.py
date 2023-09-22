def is_post_code(S, A):
    # ハイフン位置の確認
    if S[A] == "-":
        S = S[:A] + S[A + 1:]
    else:
        return False
    # 値が数字か判定
    for s in S:
        if not "0" <= s <= "9":
            return False
    return True


A, B = map(int, input().split())
S = input()
print("Yes" if is_post_code(S, A) else "No")
