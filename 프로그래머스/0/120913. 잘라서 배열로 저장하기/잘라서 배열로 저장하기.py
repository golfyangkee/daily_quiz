def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str)//n+1):
        if my_str[i*n:(i+1)*n] != '':
            answer.append(my_str[i*n:(i+1)*n])
    return answer