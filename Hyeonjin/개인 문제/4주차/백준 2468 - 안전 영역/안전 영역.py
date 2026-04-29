from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

land = []

for _ in range(n):
  line = list(map(int, input().split()))
  land.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c, k):
  q = deque()
  q.append((r, c))
  visited[r][c] = True

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

      if not visited[nx][ny] and land[nx][ny] > k:
        visited[nx][ny] = True
        q.append((nx, ny))

max_height = max(map(max, land))

answer = 0

for k in range(max_height):
  count = 0
  visited = [[False] * n for _ in range(n)]

  for row in range(n):
    for col in range(n):
      if land[row][col] > k and not visited[row][col]:
        bfs(row, col, k)
        count += 1
        
  answer = max(answer, count)

print(answer)