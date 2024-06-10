def solution(my_string):
    # answer = my_string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    # return answer

     # 다른 방식으로 풀어보기
    return ''.join(i for i in my_string if not (i in 'aeiou'))