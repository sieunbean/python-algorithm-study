import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

cnt = 0
best = 0

for r in range(n):
    for c in range(m):
        if board[r][c] != 1:
            continue

        cnt += 1
        board[r][c] = 0
        q = deque([(r, c)])
        area = 1

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dr[k]
                ny = y + dc[k]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx, ny))
                    area += 1

        if area > best:
            best = area

print(cnt)
print(best)
