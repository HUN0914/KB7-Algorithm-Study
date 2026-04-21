n = int(input())

egg = []  # 계란을 담을 리스트

for _ in range(n):
  # 내구도, 무게
  a = list(map(int, input().split()))
  egg.append(a)

count = 0 # 깨진 계란의 수

def backtracking(idx, current_count):
  global count
  # 종료조건: 가장 오른쪽에 위치한 계란을 드는 경우 종료
  if idx == n:
    count = max(count, current_count)
    return
  
  # 패스조건: 손에 든 계란이 깨졌으면 다음 계란으로
  if egg[idx][0] <= 0:
    backtracking(idx + 1, current_count)
    return
  
  hit_possible = False
  
  for i in range(n):
    # 자기 자신은 칠 수 없음
    if i == idx:
      continue

    # 이미 깨진 계란도 칠 수 없음
    if egg[i][0] <= 0:
      continue

    hit_possible = True

    current = egg[idx][0]
    next = egg[i][0]
    
    egg[idx][0] -= egg[i][1]
    egg[i][0] -= egg[idx][1]

    add = 0
    if egg[idx][0] <= 0:
      add += 1
      
    if egg[i][0] <= 0:
      add += 1

    backtracking(idx + 1, current_count + add)

    # 백트래킹은 계산을 되돌려야 함!!
    egg[idx][0] = current
    egg[i][0] = next

   # 칠 수 있는 계란이 하나도 없으면 그냥 다음으로
  if not hit_possible:
      backtracking(idx + 1, current_count)

backtracking(0, 0)

print(count)