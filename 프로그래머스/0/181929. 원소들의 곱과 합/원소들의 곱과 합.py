def solution(num_list):
    answer = 0
    result = 1
    for i in num_list:
        answer +=i
        result*=i
    if answer**2 > result:
        return 1
    return 0
