def solution(my_string):
    answer = []
    n=len(my_string)
    for i in range(0,n):
        k=my_string[i:n]
        answer.append(k)
    answer.sort()
    return answer