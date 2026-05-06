def solution(clothes):
    clothes_dict = {}
    
    for c in clothes:
        if c[1] not in clothes_dict:
            clothes_dict[c[1]] = 0
        clothes_dict[c[1]] += 1
    
    result = 1
    for v in clothes_dict.values():
        result *= (v+1)

    
    return result - 1