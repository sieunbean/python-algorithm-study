N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

max_len = 1
for i in range(N):
    for j in range(M):
        for d in range(1, min(N - i, M - j)):
            if board[i][j] == board[i][j + d] == board[i + d][j] == board[i + d][j + d]:
                max_len = max(max_len, d + 1)

print(max_len * max_len)
