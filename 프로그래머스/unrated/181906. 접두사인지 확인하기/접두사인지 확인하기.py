def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(my_string)+1):
        if is_prefix == my_string[:i+1]:
            print(my_string[:i+1])
            answer=1
            break
        else:
            answer=0
    return answer