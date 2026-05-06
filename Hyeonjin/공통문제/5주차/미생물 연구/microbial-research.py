from collections import deque

# 입력
N, Q = map(int, input().split())

# board[y][x] 형태로 사용
# 0이면 빈 칸, 숫자면 미생물 번호
board = [[0] * N for _ in range(N)]

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 격자 범위 안인지 확인하는 함수
def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


# 1. 미생물 투입 함수 (주어진 직사각형 영역을 micro_id로 덮어씀)
def inject_microbe(micro_id, x1, y1, x2, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = micro_id


# 2. 분리된 미생물 제거 함수 (BFS 사용)
def find_microbes_and_remove_split():
    # 현재 board를 BFS로 탐색해서 각 미생물이 몇 개의 덩어리로 나뉘었는지 확인한다.
    # 만약 같은 id가 2개 이상의 덩어리로 나뉘면 해당 미생물은 전부 삭제한다.

    visited = [[False] * N for _ in range(N)]

    # id별 덩어리 목록
    # components[id] = [cells1, cells2, ...]
    components = {}

    for y in range(N):
        for x in range(N):
            # 미생물이 없거나 이미 방문했을 경우 넘어가
            if board[y][x] == 0 or visited[y][x]:
                continue
            
            # 미생물 발견!! 번호 저장하기
            micro_id = board[y][x]

            q = deque()
            q.append((y, x))
            visited[y][x] = True

            # 나중에 components에 넣기 위해 정보를 저장하는 것임
            cells = [(y, x)]

            while q:
                cy, cx = q.popleft()

                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]

                    # 범위를 벗어남
                    if not in_range(ny, nx):
                        continue

                    # 이미 방문함
                    if visited[ny][nx]:
                        continue

                    # 해당 미생물이 아님
                    if board[ny][nx] != micro_id:
                        continue

                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cells.append((ny, nx))
            
            # 한 번도 발견되지 않은 미생물이라면 추가해줍니다
            if micro_id not in components:
                components[micro_id] = []
            
            # 해당 미생물에 대한 정보를 저장해줍니다. (만약 덩어리가 두 개라면 두개의 배열이 저장됨)
            components[micro_id].append(cells)
    
    # 살아남은 미생물을 저장할 딕셔너리
    microbes = {}

    '''
        components = {
            1: [[(0,0), (0,1), (1,0)]],
            2: [[(2,0), (2,1)], [(4,3), (4,4)]],
            3: [[(1,3), (1,4)]]
        }
    '''

    for micro_id, comp_list in components.items():
        # 덩어리가 2개 이상이면 분리된 것이므로 삭제
        if len(comp_list) >= 2:
            for cells in comp_list:
                for y, x in cells:
                    board[y][x] = 0
        else:
            # 덩어리가 한 개라면 딕셔너리에 저장
            microbes[micro_id] = comp_list[0]

    return microbes

# 미생물의 모양을 (0, 0) 기준으로 바꿔주는 함수 -> 모양을 체크하기 위해
def normalize_shape(cells):
    """
    예를 들어 cells가
    [(3, 4), (3, 5), (4, 4)] 라면
    최소 y = 3, 최소 x = 4 이므로
    [(0, 0), (0, 1), (1, 0)] 형태가 된다.
    """

    min_y = min(y for y, x in cells)
    min_x = min(x for y, x in cells)

    shape = []

    for y, x in cells:
        shape.append((y - min_y, x - min_x))

    return shape

# shape를 new_board의 (base_y, base_x)에 놓을 수 있는지 확인
def can_place(new_board, shape, base_y, base_x):
    # 놓여질 좌표 미리 계산해보기
    for sy, sx in shape:
        ny = base_y + sy
        nx = base_x + sx

        # 범위를 벗어남
        if not in_range(ny, nx):
            return False

        # 해당 좌표에 이미 미생물이 있다면 놓을 수 없다!!! -> False 리턴해주기
        if new_board[ny][nx] != 0:
            return False

    return True


# 3. 새 용기로 이동 함수 (넓이가 큰 미생물부터 이동 -> 넓이가 같다면 먼저 투입된 미생물부터)
def relocate_microbes(microbes):

    new_board = [[0] * N for _ in range(N)]

    # 정렬 기준: 넓이 큰 순(내림차순), 번호 작은 순(오름차순)
    micro_ids = sorted(
        microbes.keys(),
        key = lambda x: (-len(microbes[x]), x)
    )

    for micro_id in micro_ids:
        cells = microbes[micro_id]

        # 미생물 위치 (0, 0) 기준으로 바꿔주기 (모양 체크)
        shape = normalize_shape(cells)

        # 놓았는지 안놓았는지 여부
        placed = False

        # x가 작은 위치 우선, 같으면 y가 작은 위치 우선
        for base_x in range(N):
            # 이미 놓았다면 나가.
            if placed:
                break
            
            for base_y in range(N):
                # 놓을 수 있다면 새로운 보드에 미생물을 옮겨 심어줍니다
                if can_place(new_board, shape, base_y, base_x):
                    for sy, sx in shape:
                        ny = base_y + sy
                        nx = base_x + sx
                        new_board[ny][nx] = micro_id
                    
                    # 놓았다고 체크해주기
                    placed = True
                    break

        # 어디에도 못 놓으면 자동으로 사라짐 -> 왜냐? 배치를 안했기 때문이야..

    return new_board

# 4. 결과 계산 함수 (서로 다른 미생물이 맞닿아 있으면 두 미생물 넓이의 곱을 더함)
def calculate_score():
    # 딕셔너리 -> 미생물 번호: 미생물 넓이
    area = {}

    # 각 미생물의 넓이 계산
    for y in range(N):
        for x in range(N):
            micro_id = board[y][x]

            # 미생물이 없는 경우
            if micro_id == 0:
                continue
            
            # 처음 발견한 미생물이라면 딕셔너리에 추가해주어요
            if micro_id not in area:
                area[micro_id] = 0
            
            # 발견했으니 넓이 +1
            area[micro_id] += 1

    # 서로 인접한 미생물짝꿍을 찾아서 저장할 집합
    pairs = set()

    # 인접한 미생물 쌍 찾기
    for y in range(N):
        for x in range(N):
            # 미생물이 없는 경우
            if board[y][x] == 0:
                continue

            # 현재 미생물 번호 저장
            now = board[y][x]

            # 상하좌우를 둘러보자
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                # 범위를 벗어나는가
                if not in_range(ny, nx):
                    continue

                # 미생물이 없는가
                if board[ny][nx] == 0:
                    continue

                # 같은 미생물 친구인가
                if now == board[ny][nx]:
                    continue

                # 아니라면!!! (1, 2)의 형태로 집합에 넣어준다 (sort하는 이유는 (1, 2)와 (2, 1)를 같게 하기 위함)
                pair = tuple(sorted((now, board[ny][nx])))
                pairs.add(pair)

    score = 0

    # 짝꿍들을 꺼내서 넓이 합을 계산해줌
    for a, b in pairs:
        score += area[a] * area[b]

    return score


for micro_id in range(1, Q + 1):
    x1, y1, x2, y2 = map(int, input().split())

    # 1. 미생물 투입
    inject_microbe(micro_id, x1, y1, x2, y2)

    # 2. 분리된 미생물 제거
    microbes = find_microbes_and_remove_split()

    # 3. 새 용기로 이동
    board = relocate_microbes(microbes)

    # 4. 결과 계산
    print(calculate_score())