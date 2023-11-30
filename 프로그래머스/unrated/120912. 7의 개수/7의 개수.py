def solution(array):
    answer = 0
    str1=''
    for i in array:
        str1+=str(i)
    print(str1)
    answer=str1.count('7')
    return answer