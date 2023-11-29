def solution(my_string):
    answer = ''
    for i in my_string :
        if i in answer :
            continue 
        else :
            answer += i
            
    # 다른 풀이
        # return ''.join(dict.fromkeys(my_string))
    return answer