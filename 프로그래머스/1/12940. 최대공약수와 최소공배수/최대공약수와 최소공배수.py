def solution(n, m):
    answer = []
    if n>m:
        n, m = m , n
    result=[]
    for i in range(1, m+1):
        if n%i==0 and m%i==0:
            result.append(i)
    max_a = result[-1]
    answer.append(max_a)
    answer.append(n*m/max_a)
    return answer