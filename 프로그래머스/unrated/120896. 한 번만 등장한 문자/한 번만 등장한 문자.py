def solution(s):
    answer = ''
    for i in s:
        if s.count(i)==1:
            answer+=i
            answer= ''.join(sorted(answer))
    # answer=sorted(answer) 하면 ["d"] 리스트로 감싸줘서 나옴
    return answer