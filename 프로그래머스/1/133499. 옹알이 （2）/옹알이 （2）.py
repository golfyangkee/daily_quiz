def solution(babbling):
    answer = 0
    result = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in result:
            if j*2 not in i: # 연속으로 두번 반복되지 않아야 한다.
                i=i.replace(j,' ') 
                # ' '로 변경하는 이유는 "ayayeayayeaya" 인 경우 
                # aya 지우면 yeye만 남게 되니까 
                # 공백을 줘서 ' ye ye ' 이런식으로 만들어야 하니까
        if i.strip()=='': # strip은 공백을 제거한다.
            answer+=1
    return answer