def solution(babbling):
    answer = 0
    result=["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in result:
            if j*2 not in i:
                i=i.replace(j,' ')
        if i.strip() =='':
            answer+=1
    return answer