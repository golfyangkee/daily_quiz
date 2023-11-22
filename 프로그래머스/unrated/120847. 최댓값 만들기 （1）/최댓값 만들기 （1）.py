def solution(numbers):
    numbers.sort()
    max=numbers[-1]*numbers[-2]
    answer = max
    return answer