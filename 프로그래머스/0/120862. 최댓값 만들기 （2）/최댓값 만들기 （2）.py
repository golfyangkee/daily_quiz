def solution(numbers):
    result = []
    numbers.sort()
    for i in range(0,len(numbers)-1):
        result.append(numbers[i]*numbers[i+1])
    return max(result)