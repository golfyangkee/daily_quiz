def solution(my_string):
    num_list=['1','2','3','4','5','6','7','8','9']
    res=0
    for i in num_list:
        if i in my_string:
            num=int(i)*my_string.count(i)
            res=res+num
    answer = res
    return answer