def solution(my_string):
    answer = []
    result = 0
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    answer = my_string.split(' ')
    for i in answer:
        if i.isnumeric():
            result+=int(i)
    return result