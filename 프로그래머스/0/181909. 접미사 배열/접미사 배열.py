def solution(my_string):
    answer = []
    num = len(my_string)
    for i in range(num):
        answer.append(my_string[-num+i:])
    return sorted(answer)