from itertools import combinations, permutations
from collections import deque

board = [list(input().strip()) for _ in range(5)]

# 현재 조각 위치
pieces = []
for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            pieces.append((i, j))

k = len(pieces)
cells = [(i, j) for i in range(5) for j in range(5)]

# 연결 여부 확인
def is_connected(pos):
    q = deque([pos[0]])
    visited = {pos[0]}
    s = set(pos)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in s and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
    return len(visited) == len(pos)

INF = int(1e9)
answer = INF

# 모든 연결된 k칸 조합
for target in combinations(cells, k):
    if not is_connected(target):
        continue

    for perm in permutations(target):
        cost = 0
        for (x1, y1), (x2, y2) in zip(pieces, perm):
            cost += abs(x1 - x2) + abs(y1 - y2)
        answer = min(answer, cost)

print(answer)
