def solution(arr):
    # answer = []
    # answer.append(arr[0]) # 처음꺼는 무조건 들어간다.
    # for i in range(1, len(arr)):
    #     if arr[i] != arr[i-1]:
    #         answer.append(arr[i])
    # return answer

   # 다른 풀이
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue 
        # a의 마지막 값인데 a[-1:]하면 a에 아무것도 없어도 실행된다.
        answer.append(i)
    return answer
    
    
    '''
def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
            
    return answer
    '''