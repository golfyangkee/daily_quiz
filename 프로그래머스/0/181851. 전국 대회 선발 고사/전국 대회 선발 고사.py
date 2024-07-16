def solution(rank, attendance):
    answer = 0
    result = []
    for i in range(len(attendance)):
        if attendance[i] == True:
            result.append(rank[i])
    result.sort()
    answer = rank.index(result[0])*10000 + rank.index(result[1])*100 + rank.index(result[2])
    return answer