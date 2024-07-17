def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        else:
            pass
    if len(answer)<k:
        while len(answer)!=k:
            answer.append(-1)
    
    return answer[:k]