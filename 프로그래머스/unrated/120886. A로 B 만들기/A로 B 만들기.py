def solution(before, after):
    answer = 0
    for i in list(before):
        if i in list(after) and list(before).count(i)==list(after).count(i):
            answer=1
            continue
        else:
            answer=0
            break
    return answer