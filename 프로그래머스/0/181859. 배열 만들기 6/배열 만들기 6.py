def solution(arr):
    answer = []
    num = len(arr)
    i=0
    while i < num:
        if len(answer) ==0:
            answer.append(arr[i])
            i+=1
        elif len(answer) !=0 and answer[-1]==arr[i]:
            answer = answer[:-1]
            i+=1
        elif len(answer) !=0 and answer[-1]!=arr[i]:
            answer.append(arr[i])
            i+=1
    if len(answer)==0:
        return [-1]
    else:
        return answer