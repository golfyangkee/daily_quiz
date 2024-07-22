def solution(str1, str2):
    answer = ''
    num = len(str1)
    for i in range(num):
        answer+= str1[i] + str2[i]
    return answer