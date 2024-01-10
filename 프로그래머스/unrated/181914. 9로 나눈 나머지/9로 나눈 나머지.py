def solution(number):
    answer = 0
    res=0
    for i in number:
        a=int(i)
        res+=a
    answer=res%9
    return answer