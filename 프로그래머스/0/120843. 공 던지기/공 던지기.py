def solution(numbers, k):
    i=2*(k-1)
    
    return numbers[i%len(numbers)]
            