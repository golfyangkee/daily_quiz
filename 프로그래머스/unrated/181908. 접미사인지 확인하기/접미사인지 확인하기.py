def solution(my_string, is_suffix):
    for i in range(0,len(my_string)):
        if is_suffix== my_string[i:]:
            print(my_string[i:])
            answer=1
            break
        else:
            print(my_string[i:])
            answer=0
    return answer