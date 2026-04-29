from collections import deque

f, s, g, u, d = map(int, input().split())

# 이동 거리를 저장할 일차원 배열 (0으로 초기화)
dist = [1e9] * (f+1)

# 방문 체크
visited = [False] * (f+1)

q = deque()
q.append(s)
dist[s] = 0
visited[s] = True

while q:
  now = q.popleft()

  if q == g:
    break

  up = now + u
  down = now - d

  if 0 < up < f+1 and visited[up] == False:
    q.append(up)
    dist[up] = dist[now] + 1
    visited[up] = True

  if 0 < down < f+1 and visited[down] == False:
    q.append(down)
    dist[down] = dist[now] + 1
    visited[down] = True
  
if dist[g] == 1e9:
  print("use the stairs")
else:
  print(dist[g])
