def solution(n):
    res =1
    i = 1
    while res<=n:
        i+=1
        res = i*res

    return i-1