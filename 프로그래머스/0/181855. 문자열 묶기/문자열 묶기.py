def solution(strArr):
    my_list = [len(i) for i in strArr]
    answer = []
    for i in set(my_list):
        answer.append(my_list.count(i))
    return max(answer)