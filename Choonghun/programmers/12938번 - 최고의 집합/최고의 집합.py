def solution(n, s):
    if not s // n: # 몫이 0이면 집합이 존재하지 않으므로 [-1] 반환
        return [-1] 
    else:   # s를 n으로 나눈 몫을 길이 n의 배열로 만들고
        answer = [s//n for _ in range(n)] 
        for i in range(len(answer)-1, len(answer)-1-s%n, -1): #오름차순이므로 1을 s를 n으로 나눈 나머지만큼 뒤에서부터 더해준다.
            answer[i] += 1
        return answer