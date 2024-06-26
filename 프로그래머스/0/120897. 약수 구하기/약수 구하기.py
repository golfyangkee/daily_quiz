def solution(n):
    answer = []
    a = 1
    while a <= n :
        if n%a == 0:
            answer.append(a)
        a+=1
    return answer