def solution(n):
    res =1
    i = 1
    while res<=n:
        res = i*res
        i+=1
    return i-2