def solution(myString):
    answer = []
    list1=myString.split('x')
    for res in list1:
        answer.append(len(res))
    return answer