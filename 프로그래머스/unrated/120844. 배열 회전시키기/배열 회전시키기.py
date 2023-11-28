def solution(numbers, direction):
    answer = []
    if direction=='right':
        right=numbers[-1]
        numbers.remove(numbers[-1])
        numbers.insert(0,right)
        answer=numbers
    else:
        left=numbers[0]
        numbers.remove(numbers[0])
        numbers.insert(len(numbers)+1,left)
        answer=numbers
    return answer