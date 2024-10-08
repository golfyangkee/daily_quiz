def solution(n, m, section):
    answer = 1
    pre = section[0]
    for i in section:
        if pre+m-1<i:
            answer+=1
            pre=i # 덧칠한 경우 pre의 위치를 매번 변경해줘야 한다
    return answer