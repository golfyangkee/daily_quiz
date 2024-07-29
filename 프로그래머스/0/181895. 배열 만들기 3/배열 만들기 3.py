def solution(arr, intervals):
    answer = []
    for i in intervals:
        a, b = i[0], i[1]
        for i in range(a,b+1):
            answer.append(arr[i])
    return answer