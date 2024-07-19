def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        num = int(i[s:s+l])
        if k< num:
            answer.append(num)
    return answer