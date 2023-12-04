def solution(numbers):
    answer = 0
    numbers.sort()
    max_a=numbers[0]*numbers[1]
    max_b=numbers[-1]*numbers[-2]
    answer=max(max_a,max_b)
    return answer