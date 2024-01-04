def solution(myString):
    answer = []
    list1=myString.split('x')
    for i in list1:
        if i != '':
            answer.append(i)
    answer.sort()
    return answer

# 다른 풀이
# answer = ' '.join(myString.split('x')).split()
#  return sorted(answer)