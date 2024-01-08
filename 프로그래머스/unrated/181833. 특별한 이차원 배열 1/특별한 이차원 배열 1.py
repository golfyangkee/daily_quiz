def solution(n):
    # list 0으로 채우는 방법
    answer=[[0]*n for i in range(n)]
    
    for i in range(n): answer[i][i]=1
    return answer