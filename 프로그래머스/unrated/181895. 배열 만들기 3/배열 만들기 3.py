def solution(arr, intervals):
    answer = []
    a=intervals[0][0]
    b=intervals[0][1]+1
    c=intervals[1][0]
    d=intervals[1][1]+1
    list1=arr[a:b]
    list2=arr[c:d]
    answer=list1+list2
    return answer