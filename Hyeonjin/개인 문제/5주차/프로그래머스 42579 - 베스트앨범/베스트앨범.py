def solution(genres, plays):
    answer = []
    
    # 재생 횟수의 총합을 저장
    dict_sum = {}
    
    # 장르별 재생 횟수 저장
    dict_num = {}
    
    for i in range(len(genres)):
        if genres[i] not in dict_sum:
            dict_sum[genres[i]] = 0
            dict_num[genres[i]] = []
        dict_sum[genres[i]] += plays[i]
        dict_num[genres[i]].append((i, plays[i]))
    
    # 정렬하기
    sorted_sum = dict(sorted(dict_sum.items(), key = lambda x : x[1], reverse = True))
    
    # 딕셔너리에서 하나만 꺼내면 알아서 key만 나옴
    for key in dict_num:
        dict_num[key].sort(key = lambda x : x[1], reverse = True)
    
    # 재생 횟수가 높은 장르부터 정답 리스트에 추가 (슬라이싱은 인덱스 에러가 안난다!)
    for k in sorted_sum:
        for idx, _ in dict_num[k][:2]:
            answer.append(idx)   
    
    return answer