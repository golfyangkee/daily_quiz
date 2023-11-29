def solution(my_string):
    answer = ''
    my_lower=my_string.lower()
    my_list=list(my_lower)
    my_list.sort()
    for i in my_list:
        answer= answer+i
        
    # 다른 풀이
    # return ''.join(sorted(my_string.lower()))
    return answer