def solution(a, b):
    answer = 0
    res1=0
    res2=0
    res1=int(str(a)+str(b))
    res2=2*a*b
    answer=max(res1,res2)
    return answer