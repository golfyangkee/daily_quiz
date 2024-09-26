def solution(number, limit, power):
    answer = 0
    
    # 약수를 구하는 방법은 제곱근을 활용하기
    for i in range(1,number+1):
        
        hap=0
        n = int(i**(0.5)) 
        # i의 제곱근에서 정수 부분만 추출 예를 들면 i가 4이면 n = 2인거고
        # i가 26 이면 n = 5 인거다.
        
        for j in range(1,n+1):
            if i%j==0:
                hap+=1 # 나눠지면 약수
                
                # 제곱근으로 나눴을 때 나눠지면서 몫이 제곱근과 다르면 +하고 
                # 제곱근과 같다면 4//2 이런 상황이니 + 안 한다.
                if j !=i//j: 
                    hap+=1
                    
        if hap > limit:
            answer+=power
        else:
            answer+=hap
    return answer
    
    ## 시간 초과 떠서 약수를 구하는 방법 변경
    # for i in range(1,number+1):
    #     hap=0 # 각 기사들의 약수의 개수를 세기 전 초기화
    #     for j in range(1,i+1): # 각 기사들의 약수 카운트해서 개수 세기
    #         if i%j==0:
    #             hap+=1
    #     if hap > limit:
    #         answer+=power
    #     else:
    #         answer+=hap
    # return answer