def solution(my_string, queries):
    my_list = list(my_string)
    print(my_list)
    for i, j in queries:
        if i !=0:
            my_list[i:j+1] = my_list[j:i-1:-1]
        else:
            my_list[i:j+1] = my_list[j::-1]
    return ''.join(i for i in my_list)