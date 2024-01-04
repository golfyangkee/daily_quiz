def solution(myString):
    answer = ''
    answer=myString.replace('a','l').replace('b','l').replace('c','l').replace('d','l').replace('e','l').replace('f','l').replace('g','l').replace('h','l').replace('i','l').replace('j','l').replace('k','l')  
    return answer

# 다른 풀이
#    answer = [x if x > 'l' else 'l' for x in myString]
#    return ''.join(answer)