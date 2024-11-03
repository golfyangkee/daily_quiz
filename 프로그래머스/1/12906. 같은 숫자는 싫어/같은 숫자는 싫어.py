def solution(arr):
    answer = []
    answer.append(arr[0]) # 처음꺼는 무조건 들어간다.
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
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