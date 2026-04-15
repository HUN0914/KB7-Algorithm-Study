import sys
input = sys.stdin.readline

n,m = [int(i) for i in input().split()]
data = [[0 for _ in range(n+1)] for __ in range(n+1)]
blocks = [[] for _ in range(101)] # 현재 위치(x,y), height, width

# 공간 안 빠져나오는거 보장한다고 했다.
def go_down_block(idx): #블록 내리기
    fx,fy,h,w = blocks[idx] # 해당 블록 정보 가져오기 (위치, 높이, 길이)
    for i in range(fx+1, n+2): #현재 위치부터 쭉 내려가면서
        if i > n or sum(data[i][fy:fy+w]) > 0: #바닥 충돌 or 블록 충돌시
            remove_block(idx) #기존 블록 지우고
            for a in range(i-1, i-1-h if i-1-h >= 0 else 0, -1): # 새로운 위치로 이동
                for b in range(fy, fy+w):
                    data[a][b] = idx
            blocks[idx] = [i-1, fy, h, w] #블록 정보 갱신
            return

def remove_block(idx): #블록 지우기 메서드
    fx,fy,h,w = blocks[idx]
    for a in range(fx, fx-h if fx-h >= 0 else 0, -1): 
        for b in range(fy, fy+w):
            data[a][b] = 0
    return

def get_next_from_left(): #왼쪽에서 다음에 뺄 블록 찾기
    check = [0 for _ in range(101)] # 블록 조회 여부 체크
    res = 101
    for i in range(n, 0, -1): # 밑에서부터 체크
        flag = 1 # 처음 만난 블록인지 체크하는 용도의 flag
        for j in range(1,n+1): # 왼쪽에서 오른쪽으로
            if data[i][j]:
                if not check[data[i][j]] and flag: # 처음 만난 블록이고, 해당 행에서도 가장 앞에 있다면
                    res = min(res, data[i][j]) # 인덱스 값 체크
                check[data[i][j]] = 1  
                flag = 0
    return res

def get_next_from_right(): #오른쪽에서 다음에 뺄 블록 찾기 left 버전과 방향만 반대고 로직은 같다.
    check = [0 for _ in range(101)]
    res = 101
    for i in range(n, 0, -1):
        flag = 1
        for j in range(n, 0, -1): # 오른족에서 왼쪽으로
            if data[i][j]:
                if not check[data[i][j]] and flag:
                    res = min(res, data[i][j])
                check[data[i][j]] = 1      
                flag = 0              
    return res

def check_end(): #블록 정보가 아예 없으면 종료!
    return sum([len(x) for x in blocks])
    
def get_data(): #데이터 입력
    for _ in range(m):
        idx, h, w, c = [int(i) for i in input().split()] # 입력 받고
        blocks[idx] = [0, c, h, w] # 최초 x는 0으로 설정하고
        go_down_block(idx) # 밑으로 내려

def go_down_blocks(): # 로직은 블록 빼는 메서드랑 거의 비슷
    check = [0 for _ in range(101)] # 방문 체크용
    for i in range(n, 0, -1):
        for j in range(1, n+1):
            if data[i][j] and not check[data[i][j]]: # 아직 방문하지 않은 블록이면
                go_down_block(data[i][j]) # 내리고
                check[data[i][j]] = 1 # 체크
        
def print_blocks(): #디버깅용 컨테이너 출력 코드
    for x in data:
        print(x)

get_data() # 데이터 받기
while check_end():
    # part 1. 왼쪽에서 블록 제거 후 내리기
    n_left = get_next_from_left() # 왼쪽 블록
    if n_left == 101: # 101이면 아예 없다는 것이므로 종료
        break
    print(n_left) # 출력
    
    remove_block(n_left) # 컨테이너에서 블록 제거
    blocks[n_left] = [] # 정보 제거
    
    go_down_blocks() # 블록 모두 내리기
    
    # part 2. 왼쪽에서 블록 제거 후 내리기
    n_right = get_next_from_right() # 오른쪽 블록
    if n_right == 101: # 101이면 아예 없다는 것이므로 종료
        break
    print(n_right) # 출력
    
    remove_block(n_right) # 컨테이너에서 블록 제거
    blocks[n_right] = [] # 정보 제거
    
    go_down_blocks() # 블록 모두 내리기
    