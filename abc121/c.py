N, M = map(int, input().split())
price_piece = []
for i in range(N):
    price_piece.append(list(map(int, input().split())))
price_piece.sort()
need_piece = M
ans = 0

for p_p in price_piece:
    price, piece = p_p
    if need_piece > piece:
        ans += price * piece
        need_piece -= piece
    else:
        ans += need_piece * price
        break
print(ans)
