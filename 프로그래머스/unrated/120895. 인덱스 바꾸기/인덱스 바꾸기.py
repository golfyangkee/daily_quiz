def solution(my_string, num1, num2):
    answer = ''
    str1=my_string[num1]
    str2=my_string[num2]
    my_list=list(my_string)
    my_list.insert(num2,str1)
    my_list.pop(num2+1)
    my_list.insert(num1,str2)
    my_list.pop(num1+1)
    for i in my_list:
        answer += i
    return answer