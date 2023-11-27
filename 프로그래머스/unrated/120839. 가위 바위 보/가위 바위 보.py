def solution(rsp):
    answer = ''
    # si -> ba // ba -> bo // bo -> si
    # 2  -> 0  // 0  -> 5  // 5  -> 2
    # si=2
    # ba=0
    # bo=5
    dict1={'2':'0','0':'5','5':'2'}
    for i in rsp :
        answer=answer+dict1[i]
    return answer