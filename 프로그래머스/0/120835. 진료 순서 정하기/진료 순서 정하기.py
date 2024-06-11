def solution(emergency):
    answer = []
    res = sorted(emergency, reverse = True)
    for i in emergency:
        rank = res.index(i)+1
        answer.append(rank)
    return answer
        