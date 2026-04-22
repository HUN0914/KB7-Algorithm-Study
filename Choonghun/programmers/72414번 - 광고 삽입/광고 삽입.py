def solution(play_time, adv_time, logs):
    
    def timeToNum(time): # 시간을 숫자로
        data = time.split(':')
        res = 0
        res += int(data[0]) * 3600
        res += int(data[1]) * 60
        res += int(data[2])
        return res
    
    def NumTotime(num): # 숫자를 시간으로
        data = []
        data.append(str(num//3600).rjust(2, '0'))
        num %= 3600
        data.append(str(num//60).rjust(2, '0'))
        num %= 60
        data.append(str(num).rjust(2, '0'))
        return ":".join(data)
    
    end = timeToNum(play_time)
    adv = timeToNum(adv_time)
    data = [0 for _ in range(end+1)]
    for log in logs:
        st, ed = log.split('-')
        st = timeToNum(st)
        ed = timeToNum(ed)
        data[st] += 1
        data[ed] -= 1
    
    restore = [data[0]]
    for i in range(1, end+1):
        restore.append(data[i]+restore[i-1])
    
    for i in range(1, end+1):
        restore[i] += restore[i-1]
    
    res = restore[adv-1]
    answer = NumTotime(0)
    for i in range(1, end-adv+1):
        if restore[i+adv-1] - restore[i-1] > res:
            res = restore[i+adv-1] - restore[i-1]
            answer = NumTotime(i)
    
    return answer

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))