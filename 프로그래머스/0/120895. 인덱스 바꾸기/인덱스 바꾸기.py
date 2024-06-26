def solution(my_string, num1, num2):
    a = my_string[num1]
    b = my_string[num2]
    result = list(my_string)
    result[num1] = b
    result[num2] = a
    answer = ''.join(result)
    return answer