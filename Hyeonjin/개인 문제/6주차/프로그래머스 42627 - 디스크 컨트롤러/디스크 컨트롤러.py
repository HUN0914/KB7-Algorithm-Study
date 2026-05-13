import heapq

# heapq에 튜플을 넣으면 정렬 기준을 여러개 줄 수 있다.
# 소요시간 오름차순 / 요청 시각 오름차순 / 작업 번호 오름차순

def solution(jobs):
    
    # 요청 시간 순으로 정렬
    jobs.sort()
    
    heap = []
    time = 0  # 현재 시각
    idx = 0  # 다음으로 heap에 넣을 작업의 위치
    total = 0 # 각 작업의 걸린시간을 계산하는 변수
    count = 0  # 현재 처리한 작업의 수
    
    while count < len(jobs):
        
        while idx < len(jobs) and jobs[idx][0] <= time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1
        
        if heap:
            duration, request, i = heapq.heappop(heap)
            time += duration
            total += time - request
            count += 1
        else:
            # 현재 실행할 수 있는 작업이 없으면 다음 작업 요청 시간으로 점프
            time = jobs[idx][0]
             
    return total // len(jobs)