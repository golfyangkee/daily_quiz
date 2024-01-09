def solution(arr, idx):
    answer = 0
    list1=arr[idx:]
    for i in list1:
        if i==1:
            answer=list1.index(i)+idx
            break
        else:
            answer=-1
    return answer