def solution(num_list):
    answer=[]
    num_list.sort()
    for i in num_list:
        answer.append(i)
        if len(answer)==5:
            break
    return answer