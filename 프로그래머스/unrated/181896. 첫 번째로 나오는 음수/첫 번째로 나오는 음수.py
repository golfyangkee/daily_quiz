def solution(num_list):
    answer = 0
    for i in num_list:
        if i<0:
            answer= num_list.index(i)
            break
        else:
            answer=-1
            
    # 다른 풀이
    # for i in range(len(num_list)):
    #     if num_list[i]<0:return i
    # return -1
    return answer