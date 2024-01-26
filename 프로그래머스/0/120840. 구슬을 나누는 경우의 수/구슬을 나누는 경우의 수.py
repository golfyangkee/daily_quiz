def solution(balls, share):
    a=balls-share
    num1=1
    num2=1
    for i in range(balls,share,-1):
        num1*=i
    for i in range(a,1,-1):
        num2*=i
    return num1/num2