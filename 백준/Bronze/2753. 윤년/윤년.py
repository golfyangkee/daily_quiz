# 윤년은 4의 배수이면서 100의 배수가 아니거나 400의 배수
n = int(input())
if n%4 ==0:
    if n%100 !=0 or n%400==0:
        print(1)
    else:
        print(0)
else:
    print(0)