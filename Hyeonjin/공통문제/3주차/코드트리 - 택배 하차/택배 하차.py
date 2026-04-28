import sys
input = sys.stdin.readline


n, m = map(int, input().split())

# 택배를 담을 공간
space = [[0] * n for _ in range(n)]

# 박스 정보 저장
# boxes[k] = [top, left, h, w, alive]
boxes = {}

# 하차 순서 저장
answer = []

# 함수 1) 택배 초기 적재 함수
def load(k, h, w, c):
    row = 0 # 처음 시작 행 => 0 (맨 위)
    col = c - 1 # 처음 시작 열 => c - 1 (배열은 0부터 시작하니까)
    
    # 바닥에 닿을 때까지 반복
    while row + h < n:
        blocked = False # 이미 적재된 택배가 있는지 여부

        # 내려가면서 가로 체크
        for j in range(col, col + w):
            if space[row+h][j] != 0: # 이미 적재된 택배가 있다면
                blocked = True
                break
        
        if blocked: # 이미 적재된 택배가 있다면 나가.
            break
        
        row += 1 # 막히지 않았다면 하나 내려가
    
    # 해당 자리에 택배 적재하기
    for i in range(row, row+h):
        for j in range(col, col+w):
            space[i][j] = k

    # 박스 정보 저장해두기! (맨 마지막은 택배가 있는지 없는지 여부)
    boxes[k] = [row, col, h, w, True]


# 함수 2) 빈공간이 있으면 택배를 아래로 떨어뜨리는 함수
def drop():
    # 이미 움직인 택배를 저장하는 집합 (또 움직이면 안되기 때문!)
    moved = set()

    # 아래쪽 행부터 보면서 박스를 최대한 아래로 내림 (그래야 불필요한 되돌림이 없음)
    for i in range(n - 1, -1, -1):
        for j in range(n):
            k = space[i][j]

            # 아직 빈공간이거나 이미 움직였다면 넘어가
            if k == 0 or k in moved:
                continue

            # 택배가 적재되어있다면 일단 정보를 꺼내옴
            top, left, h, w, alive = boxes[k]

            # 근데 이미 없는 택배라면 넘어가
            if not alive:
                continue

            # 현재 박스 지우기
            for r in range(top, top + h):
                for c in range(left, left + w):
                    space[r][c] = 0

            # 얼마나 더 내려갈 수 있는지 계산 (아까랑 똑같은 계산임)
            new_top = top
            while new_top + h < n:
                blocked = False

                for c in range(left, left + w):
                    if space[new_top + h][c] != 0:
                        blocked = True
                        break

                if blocked:
                    break

                new_top += 1

            # 다시 채우기
            for r in range(new_top, new_top + h):
                for c in range(left, left + w):
                    space[r][c] = k

            boxes[k] = [new_top, left, h, w, True]

            # 이미 움직였으니 집합에 추가 해주기
            moved.add(k)

# 좌측 하차 함수
def left():
    # 나갈 수 있는 것들 중에 가장 작은 것을 저장할 변수
    target = None

    # 박스 정보들을 꺼내와보자
    for k in boxes:
        top, left_col, h, w, alive = boxes[k]

        # 근데 이미 없는 택배라면 넘어가
        if not alive:
            continue

        # 나갈 수 있는 없는지 여부
        can_out = True

        # 박스의 세로 범위 전체에 대해
        # 왼쪽에 있는 칸들이 전부 비어 있어야 왼쪽 하차 가능
        for r in range(top, top + h):
            for c in range(0, left_col):
                if space[r][c] != 0: # 무언가로 막혀있다면?
                    can_out = False # 못나가요
                    break
            # 나갈 수 없다면 나가        
            if not can_out:
                break
        # 나갈 수 있다면
        if can_out:
            # 처음이거나 이전 보다 더 작을 경우
            if target is None or k < target:
                target = k

    # 만약 나갈 수 있는 애가 없었으면 그냥 리턴
    if target is None:
        return

    # 가장 작은 애의 정보를 가져와
    top, left_col, h, w, alive = boxes[target]

    # 원래 있던 자리를 이제 비워줘
    for r in range(top, top + h):
        for c in range(left_col, left_col + w):
            space[r][c] = 0

    # 나감 처리
    boxes[target][4] = False

    # 답에 추가
    answer.append(target)

# 우측 하차 함수
def right():
    target = None

    for k in boxes:
        top, left_col, h, w, alive = boxes[k]

        if not alive:
            continue

        # 오른쪽 좌표 계산만 추가로 진행
        right_col = left_col + w - 1
        can_out = True

        # 박스의 세로 범위 전체에 대해
        # 오른쪽에 있는 칸들이 전부 비어 있어야 오른쪽 하차 가능
        for r in range(top, top + h):
            for c in range(right_col + 1, n):
                if space[r][c] != 0:
                    can_out = False
                    break
            if not can_out:
                break

        if can_out:
            if target is None or k < target:
                target = k

    if target is None:
        return

    top, left_col, h, w, alive = boxes[target]

    for r in range(top, top + h):
        for c in range(left_col, left_col + w):
            space[r][c] = 0

    boxes[target][4] = False
    answer.append(target)


# 초기 적재
for _ in range(m):
    k, h, w, c = map(int, input().split())
    load(k, h, w, c)

# 좌 / 우 번갈아 하차
while len(answer) < m:
    left()
    drop()

    # 중간에 택배가 다 내렸으면 종료
    if len(answer) == m:
        break

    right()
    drop()

# 출력
for k in answer:
    print(k)
