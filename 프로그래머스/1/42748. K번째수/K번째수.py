def solution(array, commands):
    answer = []
    for i, j, k in commands:
        result= sorted(array[i-1:j])
        answer.append(result[k-1])
    return answer