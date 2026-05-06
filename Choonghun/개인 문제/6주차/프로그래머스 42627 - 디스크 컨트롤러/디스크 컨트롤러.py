import heapq as hq
def solution(jobs):
    answer = 0
    job_time = [[0,0] for _ in range(len(jobs))] # 작업 시작/종료 시점 체크 2차원 배열
    times = [[] for _ in range(1001)] # 시간대별 요청 작업 목록
    jobs.sort()
    for i in range(len(jobs)): # 각 업무들에 대하여 시작 시간 기입 및 시간대별 요청 작업 추가
        st, ti = jobs[i]
        job_time[i][0] = st
        times[st].append((ti,i))
    t = 0 # 시간 변수
    x = 0 # 처리된 업무 개수
    end = 0 # 현재 업무가 끝나는 시간
    q = [] # 우선순위 큐
    while x < len(jobs): # 모든 업무를 처리할때까지
        while t <= 1000 and times[t]: # t가 1000이하일때 현재 시간의 모든 작업을 우선순위 큐에 삽입
            hq.heappush(q, times[t].pop())
        if q and end <= t: # 현재 큐에 작업이 있고, 현재 진행 중인 작업이 없다면
            ti, ind = hq.heappop(q)  # pop해서
            end = t + ti # 끝나는 시간 계산
            job_time[ind][1] = end # 기록
            x += 1 # 완료 업무 추가
        t+=1 # 시간 1 증가
     
    answer = sum([y-x for x,y in job_time]) // len(job_time) # 평균 계산
    return answer 