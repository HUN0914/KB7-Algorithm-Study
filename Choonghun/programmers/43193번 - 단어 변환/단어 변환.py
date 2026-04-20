from collections import deque

def solution(begin, target, words):
    answer = 0
    check = [0 for _ in range(len(words))]
    que = deque([(begin, 0)])
    while len(que) > 0:
        cur, t = que.popleft()
        for i in range(len(words)): # 단어 순회
            if not check[i]: # 방문하지 않은 단어에 대해서
                word = words[i]
                ind = -1
                for j in range(len(word)): # 문자열 체크
                    if word[j] != cur[j]: # 다르다면 인덱스 체크
                        if ind < 0:
                            ind = j
                        else: # 이미 다른 인덱스가 있는데 또 발견하면 정지
                            ind = -1
                            break
                if ind >= 0: # 발견한 인덱스를 큐에 삽입
                    if word == target: # 근데 얘가 target이네?
                        return t+1 # 끝
                    check[i] = 1
                    que.append((word, t+1)) 
    return answer # 끝까지 못 찾으면 0 반환