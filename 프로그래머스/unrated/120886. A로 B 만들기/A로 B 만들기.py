def solution(before, after):
    answer = 0
    for i in list(before):
        if i in list(after) and list(before).count(i)==list(after).count(i):
            answer=1
            continue
        else:
            answer=0
            break
            
    # 다른 풀이
    # def solution(before, after):
    # before=sorted(before)
    # after=sorted(after)
    # if before==after:
    #     return 1
    # else:
    #     return 0
    return answer