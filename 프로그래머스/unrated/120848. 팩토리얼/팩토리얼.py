def solution(n):
    answer = 0
    res=1
    for i in range(1,n+1):
        res=res*i
        print('res야', res)
        print('====')
        if res>n:
            answer=i-1
            break
        elif res==n:
            answer=i
            break
    return answer