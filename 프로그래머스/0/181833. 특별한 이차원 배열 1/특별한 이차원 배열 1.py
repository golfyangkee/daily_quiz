def solution(n):
    answer = []
    for i in range(n):
        result=[]
        for j in range(n):
            result.append(0)
        answer.append(result)
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if i == j:
                answer[i][j]=1
    return answer