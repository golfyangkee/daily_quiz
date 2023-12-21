def solution(num_list):
    a=num_list[-1]
    b=num_list[-2]
    if a>b:
        res=a-b
        num_list.append(res)
    else:
        res=a*2
        num_list.append(res)
    answer=num_list
    return answer