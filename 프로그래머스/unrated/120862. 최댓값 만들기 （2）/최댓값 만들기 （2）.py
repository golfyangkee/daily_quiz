def solution(numbers):
    numbers.sort()
    num1=numbers[0]*numbers[-1]
    num2=numbers[-1]*numbers[-2]
    answer=max(num1,num2)
    return answer