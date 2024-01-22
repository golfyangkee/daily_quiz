def solution(str_list):
    answer = []
    for i in str_list:
        a=str_list.index(i)
        if i == 'l':
            answer=str_list[:a]
            break
        elif i=="r":
            answer=str_list[a+1:]
            break
        else:
            answer=[]
    return answer