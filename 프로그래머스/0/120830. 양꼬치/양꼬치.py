def solution(n, k):
    m=n//10
    l=n%10
    answer = 120000*m + 12000*l + 2000*(k-m)
    return answer