def solution(n, m):
    # keypoint : 최대공약수만 알면 된다.
    # 이해해보기 : 유클리드 호제법
    answer = []
    c,d = max(n, m), min(n, m)
    # 큰 값을 c로 작은 값을 d로 변수 설정한다.
    
    t = 1
    while t>0: # 무한 반복
        t = c%d # 나머지가 t가 된다. 0이 되는 순간 무한문 탈출
        c, d = d, t
    answer = [ c, int (n*m/c)]
    return answer
    
    
    '''
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