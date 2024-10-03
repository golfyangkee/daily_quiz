def solution(s):
    answer = []
    result={} # 각 글자의 최초 인덱스를 넣을 딕셔너리
    
    for idx, i in enumerate(s):
        if i in result:
            answer.append(idx-result[i])
        else:
            answer.append(-1)
        result[i] = idx
            
    return answer