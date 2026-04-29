'''
  좌표를 어떻게 변환해야하나 오래 고민했으나 좌표의 변환은 중요하지 않은 문제였다..
  -> 좌표가 뒤집혀도 비어있는 영역은 똑같기 때문이다!!
  -> 우리는 영역을 구할 것이기 때문에 좌표 신경 안쓰고 그냥 풀면 되는 문제였음
'''

from collections import deque

m, n, k = map(int, input().split())

paper = [[0] * n for _ in range(m)]

for _ in range(k):
  x1, y1, x2, y2 = list(map(int, input().split()))

  for r in range(y1, y2):
    for c in range(x1, x2):
      paper[r][c] = 1

visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  q = deque()
  q.append((a, b))
  visited[a][b] = True

  blank = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue

      if paper[nx][ny] == 0 and not visited[nx][ny]:
        blank += 1
        visited[nx][ny] = True
        q.append((nx, ny))
  
  return blank

count = 0
size = []

for r in range(m):
  for c in range(n):
    if paper[r][c] == 0 and not visited[r][c]:
      size.append(bfs(r, c))
      count += 1

size.sort()

print(count)
print(' '.join(map(str, size)))