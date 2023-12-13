def solution(a, b):
    a_str=str(a)
    b_str=str(b)
    num1=int(a_str+b_str)
    num2=int(b_str+a_str)
    print(num1, num2)
    if num1>=num2:
        return num1
    else:
        return num2
    