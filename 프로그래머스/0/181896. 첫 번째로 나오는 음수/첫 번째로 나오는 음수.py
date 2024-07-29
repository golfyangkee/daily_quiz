def solution(num_list):
    result=[]
    for i in num_list:
        if i < 0:
            return num_list.index(i)
        elif i >=0 :
            result.append(i)
    if len(result)==len(num_list):
        return -1