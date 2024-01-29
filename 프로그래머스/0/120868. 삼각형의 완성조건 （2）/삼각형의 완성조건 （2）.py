def solution(sides):
    sides.sort()
    a=max(sides)
    b=sides[0]
    c=a-b
    cnt=0
    for i in range(c+1,a):
        cnt+=1
    for i in range(a+1,a+b+1):
        cnt+=1
    return cnt