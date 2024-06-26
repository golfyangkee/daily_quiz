def solution(s):
    answer = ''
    result = set(list(s))
    for i in result:
        if s.count(i) == 1:
            answer += i
    return ''.join(sorted(answer))
