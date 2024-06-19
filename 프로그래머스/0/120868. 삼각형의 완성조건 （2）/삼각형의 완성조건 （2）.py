def solution(sides):
    answer = []
    sides.sort()
    num = sides[-1]
    # answer 이 가장 긴 길이일 때 = num보다는 크고 sum보다는 작다.
    # num <= answer < sides[0] + num
    for i in range(num, sides[0]+num):
        answer.append(i)
    
    # num이 가장 긴 길이일 때
    # num > answer >= num - sides[0]
    for i in range(num-sides[0], num):
        answer.append(i)
    result = set(answer)
    return len(result) -1