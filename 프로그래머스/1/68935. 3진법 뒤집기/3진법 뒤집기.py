def solution(n):
    answer = ''
    
    while n>0:
        answer += str(n%3) # str에 더해버리면 자연스럽게 뒤집어짐
        n //=3 # 몫만 빼서 n값 변경
    
    return int(answer, 3) # int는 10진수로 표현하는 것인데 매개변수에 진수 넣으면 됨
    

'''
def solution(n):
    answer = ''
    
    while n > 0:
        answer += str(n%3)
        n//=3
    
    return int(answer, 3)
'''