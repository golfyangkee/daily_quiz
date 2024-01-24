def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    answer=answer[:k]
    if len(answer)<k:
        a=k-len(answer)
        for i in range(a):
            answer.append(-1)
    return answer