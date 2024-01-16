def solution(my_string, queries):
    for i, j in queries:
        if i!=0:
            my_string=my_string[:i]+my_string[j:i-1:-1]+my_string[j+1:]
        else:
            my_string=my_string[j::-1]+my_string[j+1:]
    return my_string