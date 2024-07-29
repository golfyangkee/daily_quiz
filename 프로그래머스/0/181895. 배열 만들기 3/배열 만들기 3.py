def solution(arr, intervals):
    # answer = []
    # for i in intervals:
    #     a, b = i[0], i[1]
    #     for i in range(a,b+1):
    #         answer.append(arr[i])
    # return answer

    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    return arr[a1:b1+1] + arr[a2:b2+1]