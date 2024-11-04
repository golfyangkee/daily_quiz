def solution(n, m):
    result=[] # 겹치는 숫자 넣을 리스트
    answer = [] # return 할 리스트
    
    for i in range(1,max(n,m)+1):
        if n%i==0 and m%i==0:
            result.append(i)
            
    # 최대공약수 집어 넣기
    answer.append(max(result)) 
    
    # 최소공배수는 두 수의 곱을 최대공약수로 나눈 값이다.
    answer.append(n*m/max(result)) 
    return answer
    
    
    '''
    answer = []
    if n>m:
        n, m = m , n
    result=[]
    for i in range(1, m+1):
        if n%i==0 and m%i==0:
            result.append(i)
    max_a = result[-1]
    answer.append(max_a)
    answer.append(n*m/max_a)
    return answer
    '''