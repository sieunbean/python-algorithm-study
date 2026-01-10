n, m = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = cards[i] + cards[j] + cards[k]
            if s <= m and s > ans:
                ans = s

print(ans)
