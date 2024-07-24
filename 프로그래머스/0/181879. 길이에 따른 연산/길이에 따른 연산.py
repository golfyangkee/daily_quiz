def solution(num_list):
    answer = 1
    num = len(num_list)
    if num >= 11:
        answer = sum(num_list)
    else:
        for i in num_list:
            answer *= i
    return answer