def solution(picture, k):
    answer = []
    for row in picture:
        result = ''
        for p in row:
            result+=p*k
        for i in range(k):
            answer.append(result)
    return answer